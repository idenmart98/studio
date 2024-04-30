from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_budget = models.DecimalField(decimal_places=0, max_digits=12)
    