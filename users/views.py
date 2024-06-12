from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import SESSION_KEY
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Вы вошли на сайт под ником {username}.')
                if user.user_groups.filter(name='LINE_PRODUCER').exists():
                    return redirect('tasks:task_board')
                elif user.user_groups.filter(name='ACCOUNTANT').exists():
                    return redirect('project_list')            
                else:
                    messages.error(request, 'Неверные имя и/или пароль.')
            else:
                messages.error(request, 'Неверные имя и/или пароль.')
    else:
        if request.user.is_authenticated:
            if request.user.user_groups.filter(name='LINE_PRODUCER').exists():
                return redirect('task_board')
            elif request.user.user_groups.filter(name='ACCOUNTANT').exists():
                return redirect('project_list')    
    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={'form': form})