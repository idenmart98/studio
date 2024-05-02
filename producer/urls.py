from django.urls import path
from .views import create_project, project_list, delete_project, project_detail

urlpatterns = [
    path('create/', create_project, name='create_project'),
    path('list/', project_list, name='project_list'),
    path('<int:pk>/delete/', delete_project, name='delete_project'),
    path('<int:pk>/', project_detail, name='project_detail'),
]
