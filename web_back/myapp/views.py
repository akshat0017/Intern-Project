from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def index(request):
    return render(request, "faltu.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username,password)
        user.save()
        return render(request,"faltu.html")
    return render(request,"register.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"register.html")
        else:
            return render(request, "register.html")
    return render(request,"register.html")



