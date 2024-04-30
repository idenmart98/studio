from django.shortcuts import render, redirect
from .forms import ProjectForm

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})