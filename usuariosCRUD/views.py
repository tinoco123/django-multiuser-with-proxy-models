from django.shortcuts import render, redirect
from users.models import Usuario
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse

# Create your views here.
@login_required
def listar_usuarios(request):
    if request.method == "GET" and request.user.is_administrador:
        usuarios = Usuario.objects.all()
        contexto = {'usuarios': usuarios}
        return render(request, 'usuarios.html', contexto)
    else:
        return HttpResponseForbidden("No tienes permisos para acceder a este modulo")
    

@login_required    
def agregar_usuario(request):
    if request.method == "POST" and request.user.is_administrador:
        try:
            email = request.POST.get('email')
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            password = request.POST.get('password')
            company = request.POST.get('company')
            address = request.POST.get('address')
            age = request.POST.get('age')
            extra_fields = {
                'company' : company,
                'address' : address,
                'age' : age
            }
            usuario = Usuario.objects.create_user(email, name, lastname, password, **extra_fields)
            usuario.save()
            return redirect('listar_usuarios')
        except IntegrityError:
            return render(request, 'usuarios.html', {
                    'error': "Username already exists",
                })
    else:
        return redirect('listar_usuarios') 
        
@login_required
def editar_usuario(request, usuario_id):
    return HttpResponse(usuario_id)
