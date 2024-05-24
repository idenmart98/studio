from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('task-board/', views.task_board, name='task_board'),
    path('update-task-status/', views.update_task_status, name='update_task_status'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/add-shop-list-item', views.add_shoplist_item, name='add_shoplist_item'),
]
