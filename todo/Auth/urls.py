from django.urls import path 
from .views import login , logup

urlpatterns = [

    path('login/' , login , name='login'),
    path('logup/' , logup , name='Logup')
]