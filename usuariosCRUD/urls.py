from django.urls import path
from . import views as usuarios_views

urlpatterns = [
    path("usuarios/", usuarios_views.listar_usuarios, name='listar_usuarios'),
    path("usuarios/agregar", usuarios_views.agregar_usuario, name='agregar_usuario')
]