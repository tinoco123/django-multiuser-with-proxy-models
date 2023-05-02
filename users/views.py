from django.shortcuts import render, redirect, HttpResponse
from .models import UserAccount
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def homepage(request):
    return redirect('sign_in')

def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse("Ya estas logeado")
        else:
            return render(request, 'login.html', {
                'title': 'Login'
            })
    elif request.method == "POST":
        print("FORMULARIO POST")
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, 'login.html', {
                'title': 'Login',
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return HttpResponse("Logeado correctamente")