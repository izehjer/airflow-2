from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index , name='welcome to chat room') , 
    path('<str:room_name>' , views.room , name='room') , 
]