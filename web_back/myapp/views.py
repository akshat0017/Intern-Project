from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
#from django.contrib.auth import authentication, login, logout



# Create your views here.

def index(request):
    return render(request, "index.html",{})
