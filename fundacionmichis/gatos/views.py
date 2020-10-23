from django.shortcuts import render
from . models import Gatitos 

# Create your views here.

def index(request):
    #creacion de variable, obtener datos de los gatitos
    gatos=Gatitos.objects.all()
    return render(request,'index.html', context={'gatos':gatos}) 
    