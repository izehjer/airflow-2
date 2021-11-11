from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.




def home_view( request , *args , **kwargs ):
    return render ( request , 'home.html' , {} )
    