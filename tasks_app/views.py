from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Task

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
def update_task_status(request):
    task_id = request.POST.get('task_id')
    new_status = request.POST.get('new_status')
    task = Task.objects.get(id=task_id)
    task.status = new_status
    task.save()
    return JsonResponse({'status': 'success'})