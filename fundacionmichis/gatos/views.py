from django.shortcuts import render
from . models import Gatito

# Create your views here.

def index(request):
    #creacion de variable, obtener datos de los gatitos
    gatos=Gatito.objects.all()
    return render(request,'index.html', context={'gatos':gatos}) 

def adopta(request):
    #creacion de variable, obtener datos de los gatitos
    gatos=Gatito.objects.all()
    return render(request,'adopta.html', context={'gatos':gatos}) 
    