import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Categoría')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías'
        db_table = 'categorias_de_productos'
        ordering = ['id']

class ProductType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Tipo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipo Productos'
        db_table = 'tipos_de_productos'
        ordering = ['id']

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Marca')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca de Producto'
        verbose_name_plural = 'Marcas'
        db_table = 'marcas_de_productos'
        ordering = ['id']



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Tipo de Producto')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Marca', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Precio')
    description = models.TextField(verbose_name='Descripcion')
    photo = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='foto')
    quantity = models.IntegerField(verbose_name='Cantidad Disponible', default=0)
    cantidad_vendida = models.IntegerField(default=0, verbose_name='Cantidad Vendida')

    def save(self, *args, **kwargs):
        # Genera el slug solo si el producto no tiene uno ya asignado
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']

