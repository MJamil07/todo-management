from rest_framework.response import Response
from rest_framework.decorators import api_view
from .TodoSerializer import TodoSerializer
from rest_framework import status
from .TaskSerializer import TaskSerializer
from .models import Todo , Task
from Auth.models import Users


# Create your views here.

@api_view(['POST'])
def create_new_todo(request):

    # incoming data create new todo , only come todo name
    data = request.data;

    if request.method == 'POST':
    # data dict added for currently used user
        print('sesion : ' ,request.session['user_info'])
        data['user'] = Users.objects.get(email = request.session['user_info']).id  # type: ignore
    
        todo_serialize = TodoSerializer(data = data)

        if todo_serialize.is_valid():
            todo_serialize.save()
            return Response({'status' : 'successfull'} , status = status.HTTP_200_OK )
        
        else:
            return Response({'status' : todo_serialize.error_messages} )

@api_view(['POST'])
def create_new_task(request):
    """
        In the method is used for create a new task for specificaly login user and given todo related 
    """

    # incoming data
    data = request.data;

    if request.method == 'POST':
        # convert json to queryset
        task_serialize = TaskSerializer(data = data)

        # given data is valid create the task or show the error message
        if task_serialize.is_valid():
            task_serialize.save()

            return Response({'status' : 'Task is created sucessfully'} , status=status.HTTP_200_OK)
        else:
             return Response({'status' : task_serialize.error_messages} )


