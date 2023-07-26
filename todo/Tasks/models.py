from django.db import models
from Auth.models import Users
# Create your models here.

class Todo(models.Model):
    """
        In this model used for daily created todo
    """
    todo_name = models.CharField(max_length = 20 , null = False)
    created_date = models.DateTimeField(auto_now = True , null = False)
    user = models.ForeignKey(Users , on_delete = models.CASCADE , null = False)


    def __str__(self) -> str:
        return f'{self.todo_name} , {self.user.name}'


class Task(models.Model):

    """
        In this model used for store the curresponding todo task , manage the pending and finished status also date
    """
    task_name = models.TextField(null = False)
    created_date = models.DateTimeField(auto_now = True , null = False)
    status = models.CharField(max_length = 20 , null = False , default = 'Pending')
    is_importand = models.BooleanField(default = False)
    todo = models.ForeignKey(Todo , on_delete = models.CASCADE , null = False)

    def __str__(self) -> str:
        return f'{self.task_name} , {self.status} , {self.todo.todo_name} , {self.todo.user.email}'