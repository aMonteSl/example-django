from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('suma/<int:op1>/<int:op2>', views.suma),
    path('resta/<int:op1>/<int:op2>', views.resta)
]