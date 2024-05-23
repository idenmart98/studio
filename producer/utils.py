from tasks_app.models import Task, ShopList

def create_task(category_project):
    task = Task.objects.create(
        task_type=Task.CREATE_SHOPPING_LIST,
        category=category_project,
        status=Task.TO_DO
    )
    
    ShopList.objects.create(task=task)
