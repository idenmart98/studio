from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from tasks_app.models import Task
from producer.forms import ExpenseForm
import telebot
from telebot import types
from django.shortcuts import render, redirect
from users.models import User
from .funcs import check_password
from .buttuns import main_keyboard
from tasks_app.models import ShopListItem

bot = telebot.TeleBot(settings.BOT_TOKEN)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@bot.message_handler(commands=['start'])
def start(message):
    print(0)
    try:
        User.objects.get(chat_id=message.chat.id)
        bot.send_message(
            message.chat.id,
            'Вы успешно вошли в систему',
            reply_markup=main_keyboard()
        )
    except User.DoesNotExist:
        bot.send_message(
            message.chat.id,
            'Пожалуйста, введите ваше имя пользователя:'
        )
        bot.register_next_step_handler(message, ask_for_username)
    except Exception as e:
        print(f'Unexpected error: {e}')
        
@bot.message_handler()
def handle_message(message):
    if message.text == 'Мои закупки':
        try:
            user = User.objects.get(chat_id=message.chat.id)
            tasks = Task.objects.filter(task_type=Task.BUY, status=Task.TO_DO, category__user=user)
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            for task in tasks:
                try:
                    item = ShopListItem.objects.get(id=task.item_id)
                    button = types.InlineKeyboardButton(
                        text=f"{item.name}-{item.price}", 
                        web_app=types.WebAppInfo(url=f"{settings.MAIN_URL}/bot/tasks/{task.id}/")
                    )
                    keyboard.add(button)
                except Exception as e:
                    print(f'Error while creating button for task {task.id}: {e}')
            bot.send_message(
                message.chat.id,
                'Мои закупки',
                reply_markup=keyboard
            )
        except User.DoesNotExist:
            bot.send_message(
                message.chat.id,
                'Пользователь не найден.'
            )
        except Exception as e:
            print(f'Unexpected error: {e}')
            bot.send_message(
                message.chat.id,
                'Произошла ошибка. Пожалуйста, попробуйте позже.'
            )


def ask_for_password(message, username):
    password = message.text

    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            user.chat_id = message.chat.id
            user.save()
            bot.send_message(
                message.chat.id,
                f'Вы успешно вошли в систему',
                reply_markup=main_keyboard()
                )
        else:
            bot.send_message(
                message.chat.id,
                'Неверный пароль!'
            )
    except User.DoesNotExist:
        bot.send_message(
            message.chat.id,
            'Пользователь не найден!'
        )


def ask_for_username(message):
    username = message.text
    bot.send_message(
        message.chat.id,
        'Пожалуйста, введите ваш пароль:'
    )
    bot.register_next_step_handler(
        message, lambda msg: ask_for_password(msg, username)
    )
    

@csrf_exempt
def tasks_page_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    item = get_object_or_404(ShopListItem, id=task.item_id)
    if request.method == 'GET':
        task.status = Task.IN_PROGRESS
        task.save()
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.category = task.category
            expense.shop_list_item = item  # Устанавливаем автоматически
            expense.save()
            task.status = Task.IN_PROGRESS
            task.save()
            return redirect('bot:success_page')
    else:
        form = ExpenseForm()

    return render(request, 'tasks/task_detail.html', {'task': task, 'form': form, 'item': item})

def success_page(request):
    return render(request, 'tasks/success.html')
