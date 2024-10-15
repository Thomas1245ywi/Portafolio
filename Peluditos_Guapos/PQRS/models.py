from django.db import models
from django.contrib.auth.models import User

class Tipo_pqrs(models.Model):
    Tipo_pqrs = models.CharField(max_length=30)

    def __str__(self):
        return self.Tipo_pqrs

    class Meta:
        verbose_name = 'Tipo pqrs' # Cuando se registre la BD en Django
        verbose_name_plural = 'Tipos pqrs'
        db_table = 'tipo_pqrs' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente

class Estado(models.Model):
    Estado_pqrs = models.CharField(max_length=30)

    def __str__(self):
        return self.Estado_pqrs
    
    class Meta:
        verbose_name = 'Estado_pqrs' # Cuando se registre la BD en Django
        verbose_name_plural = 'Estado pqrs'
        db_table = 'pqrs_estado' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente

class PQRS(models.Model):
    Tipo_pqrs = models.ForeignKey(Tipo_pqrs, on_delete=models.CASCADE)
    create_at = models.DateTimeField(
        auto_now=True,
        db_comment="Fecha de creacion",
        verbose_name="Fecha de creacion"
    )
    correo = models.CharField(max_length=100, verbose_name='correo electronico', blank=True, null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion')
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=True, null=True)
    Respuesta = models.TextField(max_length=500)  # Cambiado a TextField para permitir respuestas más largas
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.descripcion
    
    
    class Meta:
        verbose_name = 'PQRS' # Cuando se registre la BD en Django
        verbose_name_plural = 'PQRS'
        db_table = 'pqrs' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente
