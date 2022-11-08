"""Projeto_SAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.models import models
from app.views import index, Lista_Ruas, Create_Ruas, Update_Ruas, Delete_Ruas, home, edit_profile
from app.views import Lista_Festivais, Create_Festivais, Update_Festivais, Delete_Festivais, Add_Participante, Equipe
from django.urls import include, path

urlpatterns = [
    path('', index, name='index'),
    path('home', home),

    path('registro/', include('customauth.urls')), 
    path('edit_profile/<int:pk>/', edit_profile, name='url_edit_profile'),

    #CRUD URL RUAS
    path('Ruas/', Lista_Ruas, name='url_ruas'),
    path('Criar_Rua/', Create_Ruas, name='url_create_rua'),
    path('Editar_Rua/<int:pk>/', Update_Ruas, name="url_update_rua"),
    path('Delete_Rua/<int:pk>/', Delete_Ruas, name="url_delete_rua"),

    #CRUD URL FESTIVAIS
    path('Festivais/', Lista_Festivais, name='url_festivais'),
    path('Criar_Festival/', Create_Festivais, name='url_create_festival'),
    path('Editar_Festival/<int:pk>/', Update_Festivais, name="url_update_festival"),
    path('Delete_Festival/<int:pk>/', Delete_Festivais, name="url_delete_festival"),
    path('add_participante/<int:pk_festival>/', Add_Participante, name="url_add_participante"),
   
   
    path('Equipe - SAS/', Equipe, name="url_equipe"),
   
    
]
