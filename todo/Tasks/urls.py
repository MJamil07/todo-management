from django.urls import path
from .views import create_new_task , create_new_todo 
from .fields import my_day , pending_tasks , important_tasks , all_todos
urlpatterns = [
    
    path('create_new_todo/' , create_new_todo , name = "new todo"),
    path('create_new_task/' , create_new_task , name = "new task"),
    path('my_day/' , my_day , name = 'myday'),
    path('pending_task/' , pending_tasks , name = 'pending task'),
    path('important_tasks/' , important_tasks , name = 'important tasks'),
    path('all_todos/' , all_todos , name = 'all todos'),




]