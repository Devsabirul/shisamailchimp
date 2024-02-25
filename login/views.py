from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return render(request, 'login/signin.html',locals())
    else:
        return redirect("/")

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name') 
            username = request.POST.get('username') 
            email = request.POST.get('email') 
            password = request.POST.get('password')
            check_username = User.objects.filter(username=username).exists()
            if check_username:
                msg = "Username already exists"
            else:
                User.objects.create_user(username=username, first_name=name, email=email, password=password)
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
        return render(request, 'signup/signup.html', locals())
    else:
        return redirect("/")


def signinout(request):
    logout(request)
    return redirect('/')
