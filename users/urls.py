from django.urls import path
from . import views as user_views

urlpatterns = [
    path("", user_views.homepage, name='homepage'),
    path("login/", user_views.sign_in, name='sign_in')
]
