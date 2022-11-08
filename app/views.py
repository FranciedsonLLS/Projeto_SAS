from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy

from app.models import Rua, Festival, Participante
from app.form import RuaForm, FestivalForm

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User

from customauth.models import MyUser
from customauth.forms import UserChangeForm
# Create your views here.

def home(request, LoginRequiredMixin):
    return render(request, LoginRequiredMixin, "index.html")


def Equipe(request):
    return render(request, "nossotime.html")
    

# VIEWS DE USUARIO (READ, CREATE, UPDATE, DELETE)#

def Lista_Ruas(request):    

    parametros = {"Ruas": Rua.objects.all()}

    return render(request, "TelaRuas.html", parametros)

@login_required(login_url='auth.login')
def Create_Ruas(request):   
    formRua = RuaForm(request.POST or None)
    form = {"FormRua": formRua}

    if formRua.is_valid():
        formRua.save()
        return redirect("/Ruas")
    
    return render(request, "FormRuas.html", form)

def Update_Ruas(request, pk):
    rua = Rua.objects.get(pk=pk)
    formRua = RuaForm(request.POST or None, instance=rua)

    if formRua.is_valid():
        formRua.save()
        return redirect('url_ruas')
        
    form = {"FormRua": formRua, "rua": rua}

    return render(request, 'FormRuas.html', form)

def Delete_Ruas(request, pk):
    rua = Rua.objects.get(pk=pk)
    rua.delete()
    return redirect('url_ruas')

def index (request):
    return render(request,'index.html')


def Lista_Festivais(request):    
    festivais = Festival.objects.all()
    participantes = Participante.objects.all()
    n_participantes = {}
    count = 0    
    for festival in festivais:        
        aux = 0
        for participante in participantes:
            if participante.festival.pk == festival.pk:
                aux += 1
        n_participantes[festival.nome] = aux
        count += 1

    parametros = {"Festivais": festivais, "participantes":participantes, "n_participantes":n_participantes}
    
    return render(request, "TelaFestivais.html", parametros)

@login_required(login_url='auth.login')
def Create_Festivais(request):   
    formFestival = FestivalForm(request.POST or None)
    form = {"FormFestival": formFestival}    
    if formFestival.is_valid():
        formFestival.instance.user = request.user
        formFestival.save()
        return redirect("/Festivais")
    
    return render(request, "FormFestivais.html", form)

@login_required(login_url='auth.login')
def Update_Festivais(request, pk):
    festival = Festival.objects.get(pk=pk)
    if festival.user.id != request.user.id:
        return redirect('url_festivais')
    formFestival = FestivalForm(request.POST or None, instance=festival)

    if formFestival.is_valid():
        formFestival.save()
        return redirect('url_festivais')
        
    form = {"FormFestival": formFestival, "festival": festival}

    return render(request, 'FormFestivais.html', form)

@login_required(login_url='auth.login')
def Delete_Festivais(request, pk):
    festival = Festival.objects.get(pk=pk)    
    if festival.user.id != request.user.id:
        return redirect('url_festivais')    
    festival.delete()
    return redirect('url_festivais')

@login_required(login_url='auth.login')
def Add_Participante(request, pk_festival):
    participante = Participante.objects.filter(user=request.user, festival=pk_festival)    
    if not participante:
        festival = Festival.objects.get(pk=pk_festival)
        if request.user != festival.user:
            novo_participante = Participante.objects.create(user=request.user, festival=festival)

            novo_participante.save()
            print(participante)
        
    return redirect('url_festivais')

@login_required(login_url='auth.login')
def edit_profile(request, pk):
    user = MyUser.objects.get(pk=pk)
    if user.id == request.user.id:
        form = UserChangeForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return render(request, 'edit_profile.html', {'form': form})
    return redirect('index')
    
        
