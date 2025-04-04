# Generated by Django 5.0.2 on 2024-04-01 21:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='form_adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Nombre Completo')),
                ('age', models.PositiveIntegerField(verbose_name='Edad')),
                ('direction', models.CharField(max_length=200, verbose_name='Direccion')),
                ('city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('neighborhood', models.CharField(max_length=150, verbose_name='Barrio')),
                ('why', models.TextField(verbose_name='Razon de la Adopcion')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Respuesta')),
                ('capacityMoney', models.TextField(verbose_name='Capacidad Monetaria')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono')),
                ('work', models.TextField(verbose_name='Trabajo')),
                ('visits', models.TextField(verbose_name='Visitas')),
                ('disposition', models.TextField(verbose_name='Disposicion')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('documentFront', models.FileField(upload_to='documentos/', verbose_name='Documento Frontal')),
                ('documentBack', models.FileField(upload_to='documentos/', verbose_name='Documento Posterior')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Formulario Adopcion',
                'verbose_name_plural': 'Formularios Adopciones',
                'db_table': 'Formulario Adopcion',
                'ordering': ['id'],
            },
        ),
    ]
