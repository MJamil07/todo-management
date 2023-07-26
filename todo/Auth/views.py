
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .user_serializer import UserSerializer
from rest_framework import status
from .models import Users
# Create your views here.

@api_view(['POST'])
def login(request):
    """
        Login the existing user check if user already register or not
    """

    data = request.data
    print(data , type(data))
    if request.method == 'POST':
        # check user is already register or not

        is_exist = Users.objects.filter(email__contains = data.get('email'))
        print(is_exist)
        # given user email and password exist return that queryset len is 1 already exist or 0 not register
        if len(is_exist) == 1:

            if(is_exist[0].password == data.get('password')):
            # currently entered details stored on session 
            # request.session['user_info'] = data['email']   # type: ignore
            # print('session' , request.session['user_info'])
                return Response({"userInfo" : UserSerializer(is_exist[0]).data } , status=status.HTTP_200_OK)
            
            else :

                return Response({'status' : 'Incorrect Password'} , status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            
        return Response({"status" : 'User Not Found'} , status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def logup(request):
    """
        Register the new user  
    """
    # incoming data for user details
    data = request.data
    print(data)
    user_serilze = ''
    if request.method == 'POST':
        user_serilze = UserSerializer(data= data)

        if user_serilze.is_valid():
            user_serilze.save()

            return Response({'status' : 'success'} , status=status.HTTP_200_OK);

    print(user_serilze.error_messages) # type: ignore
    return Response('Invalid Info Please Check' , status=status.HTTP_204_NO_CONTENT)  # type: ignore
