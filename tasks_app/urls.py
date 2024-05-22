from django.urls import path
from . import views

urlpatterns = [
    path('task-board/', views.task_board, name='task_board'),
    path('update-task-status/', views.update_task_status, name='update_task_status'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]
