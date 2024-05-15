from django import forms
from .models import Project, Category, CategoryProject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'total_budget', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        
class CategoryProjectForm(forms.ModelForm):
    class Meta:
        model = CategoryProject
        fields = ['category', 'project', 'budget']
