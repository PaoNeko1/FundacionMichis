from django.db import models

# Create your models here."tablas"
class Gatito(models.Model):
    id=models.IntegerField(primary_key=True, help_text='Ingrese ID del gato')
    nombre=models.TextField(max_length=50,help_text='Ingrese nombre del gato')
    edad=models.IntegerField(help_text='Ingrese edad del gato')
    carac=models.TextField(max_length=1000, help_text='Ingrese caracteristicas del gato')
    sexo=models.CharField(max_length=50,help_text='Ingrese sexo del gato')
    imagen=models.ImageField(upload_to='imagenesgato/',null=True,blank=True)
    def __str__(self):
        return self.nombre

