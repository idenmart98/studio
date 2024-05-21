from django.db import models

# Create your models here.

class ShopList(models.Model):
    pass

class ShopListItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    shoplist = models.ForeignKey(ShopList, on_delete=models.CASCADE)


class Task(models.Model):
    BUY = 'buy'
    CREATE_SHOPPING_LIST = 'create_shopping_list'
    
    TASK_TYPE_CHOICES = [
        (BUY, 'Купить'),
        (CREATE_SHOPPING_LIST, 'Создать список покупок')   
    ]

    TO_DO = 'to_do'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    TASK_STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES, default=BUY)
    category = models.ForeignKey('producer.CategoryProject', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=TO_DO)

    def __str__(self):
        return f"{self.get_task_type_display()} - {self.get_status_display()}"