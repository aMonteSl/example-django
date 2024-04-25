from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('checklogin', views.logged_users),
    path('logout', views.logout_view),
    path('new_content', views.cms_new, name='cms_new'),
    path('<str:clave>', views.get_content, name = 'url_contenido'),
    # Aquí no se pone nada porque no llegara por el str:clave
]
