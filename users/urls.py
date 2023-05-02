from django.urls import path
from . import views as user_views

urlpatterns = [
    path("", user_views.homepage, name='homepage'),
    path("login/", user_views.sign_in, name='sign_in'),
    path("logout/", user_views.sign_out, name='sign_out')
]
