from django.contrib import admin
from .models import Administrador, Usuario, Cliente
# Register your models here.
admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Cliente)