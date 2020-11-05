# Generated by Django 3.1.2 on 2020-11-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatos', '0006_auto_20201029_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatitos',
            fields=[
                ('id', models.IntegerField(help_text='Ingrese ID del gato', primary_key=True, serialize=False)),
                ('nombre', models.TextField(help_text='Ingrese nombre del gato', max_length=50)),
                ('edad', models.IntegerField(help_text='Ingrese edad del gato')),
                ('carac', models.TextField(help_text='Ingrese caracteristicas del gato', max_length=1000)),
                ('sexo', models.CharField(help_text='Ingrese sexo del gato', max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenesgato/')),
                ('estado', models.CharField(help_text='Adoptado o huerfanito', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Padres',
            fields=[
                ('rut', models.CharField(help_text='Ingrese Rut ', max_length=9, primary_key=True, serialize=False)),
                ('nom', models.CharField(help_text='Ingrese Nombre', max_length=50)),
                ('fono', models.IntegerField(help_text='Ingrese telefono de contacto')),
                ('correo', models.CharField(help_text='Ingrese Correo', max_length=100)),
                ('dire', models.CharField(help_text='Ingrese Domicilio', max_length=100)),
                ('id', models.IntegerField(help_text='Ingrese ID del gato')),
            ],
        ),
        migrations.DeleteModel(
            name='Gatito',
        ),
    ]