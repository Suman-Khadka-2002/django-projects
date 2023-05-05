from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # gives path to the index.html
]