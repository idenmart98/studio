from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from producer.utils import create_task_ep
from .models import Task, ShopListItem, ShopList, Order, TaskEP
from .forms import ShopListItemForm

def task_board(request):
    user = request.user
    tasks_to_do = Task.objects.filter(status=Task.TO_DO, category__user=user)
    tasks_in_progress = Task.objects.filter(status=Task.IN_PROGRESS, category__user=user)
    tasks_done = Task.objects.filter(status=Task.DONE, category__user=user)

    # tasks for EP
    if user.user_groups.first().name == 'EXECUTIVE_PRODUCER':
        tasks_to_do = TaskEP.objects.filter(status=TaskEP.TO_DO)
        tasks_in_progress = TaskEP.objects.filter(status=TaskEP.IN_PROGRESS)
        tasks_done = TaskEP.objects.filter(status=TaskEP.DONE)

    return render(request, 'task_board.html', {
        'tasks_to_do': tasks_to_do,
        'tasks_in_progress': tasks_in_progress,
        'tasks_done': tasks_done,
    })


@require_POST
@csrf_exempt
def update_task_status(request):
    task_id = request.POST.get('task_id')
    new_status = request.POST.get('new_status')
    task = Task.objects.get(id=task_id)
    task.status = new_status
    task.save()

    # create task EP
    if task.status == Task.DONE:
        create_task_ep(task)

    return JsonResponse({'status': 'success'})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.status == Task.TO_DO:
        task.status = Task.IN_PROGRESS
        task.save()
    shoplist, _ = ShopList.objects.get_or_create(task=task)
    shoplist_items = ShopListItem.objects.filter(shoplist=shoplist)

    return render(request, 'task_detail.html', {
        'task': task,
        'shoplist_items': shoplist_items,
    })

def add_shoplist_item(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    shoplist, created = ShopList.objects.get_or_create(task=task)

    if request.method == 'POST':
        form = ShopListItemForm(request.POST)
        if form.is_valid():
            shoplist_item = form.save(commit=False)
            shoplist_item.shoplist = shoplist
            shoplist_item.save()
            return redirect('tasks:task_detail', task_id=task_id)
    else:
        form = ShopListItemForm()

    return render(request, 'add_shoplist_item.html', {'form': form, 'task': task})

@login_required
def get_shop_list(request):
    shoplists = ShopList.objects.filter(task__category__user=request.user)
    shoplist_items = ShopListItem.objects.filter(shoplist__in=shoplists)

    if request.method == 'POST':
        selected_items = request.POST.getlist('items')
        if selected_items:
            order = Order.objects.create()  # создаем новый заказ
            for item_id in selected_items:
                item = ShopListItem.objects.get(id=item_id)
                order.items.add(item)
            order.save()
            return redirect('tasks:kanban_board')  # перенаправление на страницу канбан-доски после создания заказа

    return render(request, 'shop_list.html', {'shoplist_items': shoplist_items})

    
    
@login_required
def kanban_board(request):
    orders_backlog = Order.objects.filter(status='backlog')
    orders_progress = Order.objects.filter(status='progress')
    orders_done = Order.objects.filter(status='done')
    
    return render(request, 'kanban_board.html', {
        'orders_backlog': orders_backlog,
        'orders_progress': orders_progress,
        'orders_done': orders_done,
    })