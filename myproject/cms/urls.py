from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('checklogin', views.logged_users),
    path('logout', views.logout_view),
    path('<str:clave>', views.get_content),
    
]
