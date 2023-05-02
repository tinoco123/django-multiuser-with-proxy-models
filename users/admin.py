from django.contrib import admin
from .models import Administrador, Usuario, Cliente, UserAccount
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Cliente)