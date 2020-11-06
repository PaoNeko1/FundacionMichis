"""fundacionmichis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#conectado con views
from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
urlpatterns = [
    path('', views.index, name='index'),
    path('adopta/', views.adopta, name='adopta'),
    path('voluntario/', views.voluntario, name='voluntario'),
    path('socio/', views.socio, name='socio'),
    path('donar/', views.donar, name='donar'),
    path('exitoend/', views.exito, name='exito'),
    path('padres/', views.PadresCreate.as_view(), name='padres'),
    path('exitoend2/', views.exito, name='exito2'),
    path('gatitos/', views.GatitosCreate.as_view(), name='gatitos'),
    path('gatitos/<int:pk>/update/', views.GatitosUpdate.as_view(), name='gatitos_update'),
    path('gatitos/<int:pk>/delete/', views.GatitosDelete.as_view(), name='gatitos_delete'),
    path('login/',login,{'templates_name':'login.html'}, name='login')
    #path('logout/',logout_then_login, name='logout')
]

