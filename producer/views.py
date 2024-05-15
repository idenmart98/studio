from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, CategoryForm, CategoryProjectForm
from .models import Project, CategoryProject

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

def project_list(request):
    projects = Project.objects.all().order_by('deadline')
    return render(request, 'project_list.html', {'projects': projects})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_categories = CategoryProject.objects.filter(project_id=pk)
    return render(request, 'project_detail.html', {'project': project, 'project_categories': project_categories})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})


def create_project_category(request, pk):  # Добавлен project_id в параметры
    project = get_object_or_404(Project, pk=pk)  # Получаем объект проекта по ID

    if request.method == 'POST':
        form = CategoryProjectForm(request.POST)
        if form.is_valid():
            category_project = form.save(commit=False)
            category_project.project = project  # Присваиваем проект категории проекта
            category_project.save()
            return redirect('project_detail', pk=pk)  # Перенаправляем на страницу деталей проекта
    else:
        form = CategoryProjectForm(initial={'project': project})  # Предварительно заполняем форму проектом

    return render(request, 'create_category_project.html', {'form': form})

