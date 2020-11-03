from django.shortcuts import render
from . models import Gatitos

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



