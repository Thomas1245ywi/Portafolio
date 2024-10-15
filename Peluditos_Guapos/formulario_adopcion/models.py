from django.db import models
from users.models import User
from CajaMascotas.models import AdoptBox
from django.core.validators import FileExtensionValidator




# Create your models here.





class form_adoption(models.Model):
    user = models.ForeignKey(User, null=False, blank= False, on_delete=models.CASCADE, verbose_name='usuario')
    full_name = models.CharField(max_length=200, verbose_name='Nombre Completo')
    documentFront = models.ImageField(max_length=200, verbose_name='Documento Cara Delantera',
                                 validators=[
                                     FileExtensionValidator(allowed_extensions=['jpeg'])
                                 ], upload_to='images/')
    documentBack = models.ImageField(max_length=200, verbose_name='Documento Cara Trasera',
                                 validators=[
                                     FileExtensionValidator(allowed_extensions=['jpeg'])
                                 ],upload_to='images/')
    age = models.PositiveIntegerField(verbose_name='Edad')
    direction = models.CharField(max_length=200, verbose_name='Direccion')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    neighborhood = models.CharField(max_length=150, verbose_name='Barrio')
    phone = models.CharField(max_length=15, verbose_name='Celular')
    why =  models.TextField(verbose_name='Razon de la Adopcion')
    work =  models.TextField(verbose_name='¿Describa su trabajo?')
    capacityMoney = models.TextField(verbose_name='¿Considera que puede mantener una mascota con su salario actual?')
    time = models.TextField(verbose_name="¿Sus responsabilidades le permiten tener tiempo de calidad con la mascota?")
    visits = models.TextField(verbose_name="¿Esta dispuesto a recibir visitas mensuales para validar que la mascota se encuentre bien ?")
    disposition = models.TextField(verbose_name="¿Esta dispuesto a Firmar un contrato de adopcion?")





    answer  =  models.TextField(verbose_name='Respuesta', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.full_name

    class Meta:
        verbose_name = 'Formulario Adopcion' # Cuando se registre la BD en Django
        verbose_name_plural = 'Formularios Adopciones'
        db_table = 'Formulario Adopcion' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente