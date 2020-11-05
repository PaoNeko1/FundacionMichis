from django.shortcuts import render, redirect, get_object_or_404
from . models import Gatitos, Padres, Usuario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .forms import PadresForm
# Create your views here.

def index(request):
    #creacion de variable, obtener datos de los gatitos
    gatos=Gatitos.objects.all()
    return render(request,'index.html', context={'gatos':gatos}) 

def adopta(request):
    #creacion de variable, obtener datos de los gatitos
    gatos=Gatitos.objects.all()
    return render(request,'adopta.html', context={'gatos':gatos}) 

def usuario(request, cate1):
    cate=cate1
    return render(request,'usuario.html', context={'cate':cate})

def donar(request):
    return render(request,'donar.html')


class PadresDelete(DeleteView):
    model = Padres
    success_url = reverse_lazy('index')

class PadresDetailView(generic.DetailView):
    model = Padres


class PadresCreate(CreateView):
    model = Padres
    fields = '__all__'


def exito(request):
    return render(request,'exito.html') 

class GatitosDelete(DeleteView):
    model = Gatitos
    success_url = reverse_lazy('index')

class GatitosDetailView(generic.DetailView):
    model = Gatitos


class GatitosCreate(CreateView):
    model = Gatitos
    fields = '__all__'

class GatitosUpdate(UpdateView):
    model = Gatitos
    fields = '__all__'
    template_name_suffix = '_update_form'

def exito2(request):
    return render(request,'exito2.html') 

class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('index')

class UsuarioDetailView(generic.DetailView):
    model = Usuario


class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'


def exito1(request):
    return render(request,'exito1.html') 