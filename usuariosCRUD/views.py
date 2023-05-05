from django.shortcuts import render, redirect
from users.models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def listar_usuarios(request):
    if request.method == "GET" and request.user.is_administrador:
        usuarios = Usuario.objects.all()
        contexto = {'usuarios': usuarios}
        return render(request, 'usuarios.html', contexto)
    else:
        return HttpResponseForbidden("No tienes permisos para acceder a este modulo")