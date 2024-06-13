from django.db import models

# Create your models here.

class ShopList(models.Model):
    task = models.OneToOneField('tasks_app.Task', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    category_project = models.OneToOneField(
        'producer.CategoryProject', on_delete=models.CASCADE, blank=True, null=True
        )  

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

    def update_status(self, new_status):
        self.status = new_status
        self.save()

    def add_comment(self, comment_text):
        Comment.objects.create(task=self, comment=comment_text)
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('backlog', 'Backlog'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    items = models.ManyToManyField(ShopListItem, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='backlog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class Comment(models.Model):
    comment = models.TextField()
    task = models.ForeignKey('tasks_app.Task', on_delete=models.CASCADE)

    
class TaskEP(models.Model):
    """
    Executive Producer Task Model
    """
    ORDER = 'order'
    SHOPLIST = 'shoplist'
    
    TASK_TYPE_CHOICES = [
        (ORDER, 'Заявка'),
        (SHOPLIST, 'Список покупок')   
    ]

    TO_DO = 'to_do'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    TASK_STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES, default=ORDER)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=TO_DO)
    task_id = models.PositiveIntegerField(unique=True)
    

    def __str__(self):
        return f"{self.get_task_type_display()} - {self.get_status_display()}"

    def update_status(self, new_status):
        self.status = new_status
        self.save()

    def add_comment(self, comment_text):
        Comment.objects.create(task_id=self.task_id, comment=comment_text)