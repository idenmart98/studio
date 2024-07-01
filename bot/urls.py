from django.urls import path, include
from .views import webhook, tasks_page_detail, success_page

app_name = 'bot'

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
    path('tasks/<int:pk>/', tasks_page_detail, name='tasks_page_detail'),
    path('success/', success_page, name='success_page'),
]
