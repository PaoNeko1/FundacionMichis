from django.db import models
from django.urls import reverse
from uuid import uuid4

# Create your models here."tablas"
class Gatitos(models.Model):
    id=models.IntegerField(primary_key=True, help_text='Ingrese ID del gato')
    nombre=models.CharField(max_length=50,help_text='Ingrese nombre del gato')
    edad=models.IntegerField(help_text='Ingrese edad del gato')
    carac=models.TextField(max_length=1000, help_text='Ingrese caracteristicas del gato')
    sexo=models.CharField(max_length=50,help_text='Ingrese sexo del gato')
    imagen=models.ImageField(upload_to='imagenesgato/',null=True,blank=True)
    estado=models.CharField(max_length=50, help_text='Adoptado o huerfanito')

    class Meta:
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('exito2')

class Usuario(models.Model):
    rut=models.CharField(primary_key=True,max_length=9,help_text='Ingrese Rut ')
    nom=models.CharField(max_length=50, help_text='Ingrese Nombre')
    contra=models.CharField(max_length=100, help_text='Ingrese Contraseña')
    fono=models.IntegerField(help_text='Ingrese telefono de contacto')
    correo=models.CharField(max_length=100,help_text='Ingrese Correo')
    cate=models.CharField(max_length=50,help_text='Ingrese si es Donador, Socio o Voluntario')

    class Meta:
        ordering=['nom']
    
    def __str__(self):
        return self.rut

    def get_absolute_url(self):
        return reverse('exito1')

class Padres(models.Model):
    rut=models.CharField(max_length=9,help_text='Ingrese Rut ')
    nom=models.CharField(max_length=50, help_text='Ingrese Nombre')
    fono=models.IntegerField(help_text='Ingrese telefono de contacto')
    correo=models.CharField(max_length=100,help_text='Ingrese Correo')
    dire=models.CharField(max_length=100,help_text='Ingrese Domicilio')
    idgatos=models.ForeignKey('Gatitos', on_delete=models.SET_NULL, null=True, blank=False)
    idadop=models.UUIDField(primary_key=True, default=uuid4, help_text='Ingrese ID de adopción')

    class Meta:
        ordering=['nom']
    
    def __str__(self):
        return self.rut

    def get_absolute_url(self):
        return reverse('exito')