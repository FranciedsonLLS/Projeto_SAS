from django.forms import ModelForm
from .models import Rua, Festival 
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _

##Criando USUARIO

class RuaForm(ModelForm):
    class Meta:
        model = Rua
        fields = ['nome', 'foto', 'descricao']

class FestivalForm(ModelForm):
    class Meta:
        model = Festival
        fields = ['nome', 'foto', 'descricao', 'rua']
        widgets = {
            'nome':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome'
                },
            ),

            'foto':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL da Foto'
                },
            ),

            'descricao':forms.TextInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Descrição'
                },
            ),

            'rua':forms.Select(
                attrs={
                    'class': 'form-control ',
                    
                    

                },
            ),
        }
        labels ={
            'nome': _(''),
            'foto': _(''),
            'descricao': _(''),
            'rua': _('Rua:'),
        }
       
    


    