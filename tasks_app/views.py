from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, ShopList
from .forms import ShopListItemForm

def task_board(request):
    tasks_to_do = Task.objects.filter(status=Task.TO_DO)
    tasks_in_progress = Task.objects.filter(status=Task.IN_PROGRESS)
    tasks_done = Task.objects.filter(status=Task.DONE)
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
    return JsonResponse({'status': 'success'})

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

@login_required
def add_shoplist_item(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    shoplist = get_object_or_404(ShopList, task=task)
    
    if request.method == 'POST':
        form = ShopListItemForm(request.POST)
        if form.is_valid():
            shoplist_item = form.save(commit=False)
            shoplist_item.shoplist = shoplist
            shoplist_item.save()
            return redirect('task_detail', pk=task_id)
    else:
        form = ShopListItemForm()
    
    return render(request, 'add_shoplist_item.html', {'form': form, 'task': task})
    
