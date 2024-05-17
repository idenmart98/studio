from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_budget = models.DecimalField(decimal_places=0, max_digits=12)
    deadline = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name

 
class CategoryProject(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        'users.User',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='category_projects')
    budget = models.DecimalField(decimal_places=0, max_digits=12, default=0)
    