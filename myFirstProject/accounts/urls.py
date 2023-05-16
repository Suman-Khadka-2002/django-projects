from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'), # gives path to the register.html
    path('login', views.login, name= 'login'),
]