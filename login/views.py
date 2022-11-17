from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return render(request, 'login/signin.html')
    else:
        return redirect("/")


def signinout(request):
    logout(request)
    return redirect('/')
