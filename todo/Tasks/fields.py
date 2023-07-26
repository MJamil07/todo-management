from rest_framework.decorators import api_view
from .TaskSerializer import TaskSerializer
from .TodoSerializer import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from Auth.models import Users 
from .models import Todo , Task

@api_view(['GET'])
def my_day(request):
    """
        When user click my-day field  show an recently create todo and tasks for specific users
    """
    print('request get -> ' , request.GET)
    print('request body -> ' , request.body)
    # request.session['user_info'] = 'jamil12@gmail.com'
    current_user = get_current_user_info(request)
    # get last created todo
    current_user_last_create_todo = Todo.objects.filter(user = current_user.id).last()  # type: ignore
    serialize_todo = TodoSerializer(current_user_last_create_todo)
 

    # filter last created todo tasks
    last_created_todo_tasks = Task.objects.filter(todo = current_user_last_create_todo.id)  # type: ignore
    serialize_task = TaskSerializer(last_created_todo_tasks , many = True)
    
    context = {
        'todo' : serialize_todo.data,
        'tasks' : serialize_task.data
    }
    return Response(context , status= status.HTTP_200_OK)

@api_view(['GET'])
def pending_tasks(request):

    """
        get all pending tasks from all todo
    """
    
    print('pending task')
    # fetching all todo from current user
    current_user_todos = get_current_user_todos(request)

    # fetching the todo all pending tasks
    todo_pending_tasks = filtered_tasks(current_user_todos , pending=True)
 
    return Response(todo_pending_tasks , status=status.HTTP_200_OK)

@api_view(['GET'])
def important_tasks(request):

    """
        fetch the all important tasks from todo
    """
    # fetching all todo from current user
    current_user_todos = get_current_user_todos(request)

    # fetching the todo important tasks
    todo_important_task = filtered_tasks(current_user_todos , important=True)
    return Response(todo_important_task , status=status.HTTP_200_OK)

@api_view(['GET'])
def all_todos(request):
    """
     Fetch the all todo and tasks 
    """

     # fetching all todo from current user
    current_user_todos = get_current_user_todos(request)

    all_todos_tasks = filtered_tasks(current_user_todos)
    return Response(all_todos_tasks , status=status.HTTP_200_OK)

def get_current_user_info(request) -> Users:
    return Users.objects.get(email = request.session['user_info'])

def get_current_user_todos(request):


    current_user = get_current_user_info(request)

    # fetching all todo from current user
    current_user_todos = Todo.objects.filter(user = current_user.id)  # type: ignore

    return current_user_todos

def filtered_tasks(todos , pending = False , important = False ):

    """
        filtered tasks for important or pending , if pending is true filtered pending task ,
          or important is True filtered important task , incase pending and important is false 
          get all tasks 
    """


    todo_and_tasks = list()

    tasks = []
    # fetching the todo all pending tasks or important or complete tasks
    for todo in todos:
        
        # if pending is true filtered pending task
        if pending:
            tasks = Task.objects.filter(todo = todo.id , status = 'Pending')  # type: ignore

        # if important is true filtered important task
        elif important:
            tasks = Task.objects.filter(todo = todo.id , is_importand = True)  # type: ignore

        #  else get all tasks
        else:
            tasks = Task.objects.filter(todo = todo.id)

        # In todo incase no pending or important tasks ignore it..
        if len(tasks) != 0:
           todo_and_tasks.append(
               {
                'todo' : TodoSerializer(todo).data,
                'task' : TaskSerializer(tasks , many = True).data
               }
           )  # type: ignore

    return todo_and_tasks;
