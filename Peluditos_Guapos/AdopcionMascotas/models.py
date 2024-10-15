import uuid

from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save




class StatePet(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nombre')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado Mascota' # Cuando se registre la BD en Django
        verbose_name_plural = 'Estados Mascotas'
        db_table = 'Estado Mascota' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente

class Type(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nombre')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo Mascota' # Cuando se registre la BD en Django
        verbose_name_plural = 'Tipo Mascotas'
        db_table = 'Tipo Mascota' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente

class Race(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Raza' # Cuando se registre la BD en Django
        verbose_name_plural = 'Razas'
        db_table = 'Raza' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente
    
   
class Pet(models.Model):
    
    plate = models.CharField(max_length=6,verbose_name='Placa')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    age = models.PositiveIntegerField(verbose_name='Edad')
    description_short = models.TextField(verbose_name='Breve Descripcion')
    description = models.TextField(verbose_name='Descripcion')
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Tipo')
    race = models.ForeignKey(Race, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Raza')
    StatePet = models.ForeignKey(StatePet, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Estado')
    photo = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='foto')
    slug = models.SlugField(null=False, blank=False, unique=True)




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mascota' # Cuando se registre la BD en Django
        verbose_name_plural = 'Mascotas'
        db_table = 'Mascota' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente




# crea el slug automatico con el nombre de la mascota
def set_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        slug = slugify(instance.name)
        while Pet.objects.filter(slug = slug).exists():
            slug = slugify(
                #cuando ese nombre exista crearemos el nombre mas un codigo especial 
                '{},{}'.format(instance.name, str(uuid.uuid4())[:8] )
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Pet)



        




