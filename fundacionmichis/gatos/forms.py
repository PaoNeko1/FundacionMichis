from django import forms
from . models import Gatitos, Padres

#PARA CREAR EL FORMULARIO PADRES
class PadresForm(forms.ModelForm):
    rut = forms.CharField(label='Rut',max_length=9, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    nom = forms.CharField(label='Nombre',max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    fono = forms.CharField(label='Telefono',max_length=9, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    correo = forms.CharField(label='Correo',max_length=9, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    dire = forms.CharField(label='Direccion',max_length=9, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    idgatos = forms.ModelChoiceField(queryset=Gatitos.objects.all(), label='Gatitos',
        widget=forms.Select(
        attrs={
                'class':'form-control' 
        }
    ))

    class Meta:
        model = Padres
        fields = '__all__'


#PARA CREAR EL FORMULARIO GATITOS
class GatitosForm(forms.ModelForm):
    id = forms.IntegerField(label='id', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombre = forms.CharField(label='nombre',max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    edad = forms.IntegerField(label='edad', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    carac = forms.CharField(label='caracteristicas',max_length=1000, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    sexo = forms.CharField(label='sexo',max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    estado = forms.CharField(label='estado',max_length=50, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    imagen = forms.ImageField(label='imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))


    class Meta:
        model = Gatitos
        fields = ('id','nombre','edad','carac','sexo','estado','imagen')

