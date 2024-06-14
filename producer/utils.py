from tasks_app.models import Task, ShopList, TaskEP

def create_task(category_project):
    task = Task.objects.create(
        task_type=Task.CREATE_SHOPPING_LIST,
        category=category_project,
        status=Task.TO_DO
    )
    
    ShopList.objects.create(task=task)

def create_task_ep(task):
    """
    Create task for Executive Producer
    """
    TaskEP.objects.create(
        task_type=TaskEP.ORDER,
        status=TaskEP.TO_DO,
        task_id=task.id
    )