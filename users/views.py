from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated and not request.user.is_superuser:
            return HttpResponse('ya estas logeado')
        else:
            return render(request, 'login.html', {
                'title': 'Login'
            })
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return render(request, 'login.html', {
                'title': 'Login',
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            if user.is_administrador:
                return redirect('listar_usuarios')
            elif user.is_usuario:
                return render(request, 'clientes.html', {
                    'title': 'Lista de usuarios'
                })
            elif user.is_cliente:
                return HttpResponse("Lista de keywords")


def sign_out(request):
    logout(request)
    return redirect('sign_in')


