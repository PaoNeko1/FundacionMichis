# Generated by Django 3.1.2 on 2020-10-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatos', '0003_auto_20201022_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gatito',
            fields=[
                ('id', models.IntegerField(help_text='Ingrese ID del gato', primary_key=True, serialize=False)),
                ('nombre', models.TextField(help_text='Ingrese nombre del gato', max_length=50)),
                ('edad', models.IntegerField(help_text='Ingrese edad del gato')),
                ('carac', models.TextField(help_text='Ingrese caracteristicas del gato', max_length=1000)),
                ('sexo', models.CharField(help_text='Ingrese sexo del gato', max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenesgato/')),
            ],
        ),
        migrations.DeleteModel(
            name='Gatitos',
        ),
    ]