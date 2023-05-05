from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.query import QuerySet


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, lastname, password=None, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("El campo de email es requerido")
        if not password or len(password) <= 0:
            raise ValueError("El campo de contraseña es requerido")

        user = self.model(email=self.normalize_email(email), name=name, lastname=lastname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, lastname, password=None, **extra_fields):
        user = self.create_user(email=self.normalize_email(email), name= name, lastname=lastname, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    class Categories(models.TextChoices):
        ADMINISTRADOR = "ADMINISTRADOR", "administrador"
        USUARIO = "USUARIO", "usuario"
        CLIENTE = "CLIENTE", "cliente"

    category = models.CharField(
        max_length=13, choices=Categories.choices)
    email = models.EmailField(
        max_length=64, unique=True, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=30, blank=True, null=True)
    date_joined = models.DateTimeField(
        auto_now_add=True, blank=True, null=False)

    is_active = models.BooleanField(default=True)
    # Para acceder al panel de administracion de Django
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Permisos especiales que definen el rol del usuario del sistema
    # Si tiene el rol de administrador dentro de la logica de negocio del programa
    is_administrador = models.BooleanField(default=False)
    is_usuario = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "lastname"]
    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)
    
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True


class AdministradorManager(models.Manager):

    def create_user(self, email, name, lastname, password=None, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("El campo de email es requerido")
        if not password:
            raise ValueError("El campo de contraseña es requerido")

        email = email.lower()
        user = self.model(email=email.lower(), name=name, lastname=lastname, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(
            category=UserAccount.Categories.ADMINISTRADOR)
        return queryset


class Administrador(UserAccount):
    class Meta:
        proxy = True
    objects = AdministradorManager()

    def save(self, *args,  **kwargs):
        self.category = UserAccount.Categories.ADMINISTRADOR
        self.is_administrador = True
        return super().save(*args,  **kwargs)


class UsuarioManager(models.Manager):
    def create_user(self, email, name, lastname, password=None, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("El campo de email es requerido")
        if not password:
            raise ValueError("El campo de contraseña es requerido")

        email = email.lower()
        user = self.model(email=email.lower(), name=name, lastname=lastname, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category=UserAccount.Categories.USUARIO)
        return queryset


class Usuario(UserAccount):
    class Meta:
        proxy = True
    objects = UsuarioManager()

    def save(self, *args,  **kwargs):
        self.category = UserAccount.Categories.USUARIO
        self.is_usuario = True
        return super().save(*args,  **kwargs)


class ClienteManager(models.Manager):
    def create_user(self, email, name, lastname, password=None, **extra_fields):
        if not email or len(email) <= 0:
            raise ValueError("El campo de email es requerido")
        if not password:
            raise ValueError("El campo de contraseña es requerido")

        email = email.lower()
        user = self.model(email=email.lower(), name= name, lastname=lastname, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category=UserAccount.Categories.CLIENTE)
        return queryset


class Cliente(UserAccount):
    class Meta:
        proxy = True
    objects = ClienteManager()

    def save(self, *args,  **kwargs):
        self.category = UserAccount.Categories.CLIENTE
        self.is_cliente = True
        return super().save(*args,  **kwargs)
