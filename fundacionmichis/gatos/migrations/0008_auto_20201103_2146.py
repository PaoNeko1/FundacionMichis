# Generated by Django 3.1.2 on 2020-11-04 00:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gatos', '0007_auto_20201102_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='padres',
            name='idadop',
            field=models.UUIDField(default=uuid.uuid4, help_text='Ingrese ID de adopción', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gatitos',
            name='nombre',
            field=models.CharField(help_text='Ingrese nombre del gato', max_length=50),
        ),
        migrations.AlterField(
            model_name='padres',
            name='rut',
            field=models.CharField(help_text='Ingrese Rut ', max_length=9),
        ),
    ]
