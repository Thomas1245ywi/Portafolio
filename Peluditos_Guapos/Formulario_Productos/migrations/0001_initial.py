

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Nombre Completo')),
                ('phone', models.PositiveIntegerField(verbose_name='Teléfono')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('neighborhood', models.CharField(max_length=150, verbose_name='Barrio')),
                ('estado_envio', models.CharField(choices=[('En proceso', 'En proceso'), ('Enviado', 'Enviado')], default='En proceso', max_length=20, verbose_name='Estado de Envío')),
                ('fecha_compra', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de compra')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
