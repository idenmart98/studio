from django.urls import path
from .views import create_project

urlpatterns = [
    path('create/', create_project, name='create_project'),
]
