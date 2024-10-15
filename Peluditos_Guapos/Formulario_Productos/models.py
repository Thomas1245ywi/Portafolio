from django.db import models
from users.models import User
from CarroProductos.models import ProductBox
from django.utils import timezone

class FormularioProducto(models.Model):
    # opciones para el estado del envío
    ESTADO_ENVIO_CHOICES = (
        ('En proceso', 'En proceso'),
        ('Enviado', 'Enviado'),
    )

    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Usuario')
    full_name = models.CharField(max_length=200, verbose_name='Nombre Completo')
    phone = models.PositiveIntegerField(verbose_name='Teléfono')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    neighborhood = models.CharField(max_length=150, verbose_name='Barrio')
    estado_envio = models.CharField(max_length=20, choices=ESTADO_ENVIO_CHOICES, default='En proceso', verbose_name='Estado de Envío')
    fecha_compra = models.DateTimeField(default=timezone.now, verbose_name='Fecha de compra')