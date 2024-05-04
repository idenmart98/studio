from django.urls import path
from .views import (
    create_project, 
    project_list, 
    delete_project, 
    project_detail, 
    edit_project,
    create_category
    )

urlpatterns = [
    path('create/', create_project, name='create_project'),
    path('', project_list, name='project_list'),
    path('<int:pk>/delete/', delete_project, name='delete_project'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('edit/<int:pk>/', edit_project, name='edit_project'),
    path('create/category', create_category, name='create_category'),

]
