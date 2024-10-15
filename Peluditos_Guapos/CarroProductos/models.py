from django.db import models
from users.models import User
from Productos.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

class ProductBox(models.Model):
    box_id = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="ID del Carrito")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuario")
    products = models.ManyToManyField(Product, through='ProductInBox', verbose_name="Productos")
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name="Sub Total")
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name="Total")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    def __str__(self):
        return self.box_id
    
    class Meta:
        verbose_name = 'Carro Productos'
        verbose_name_plural = 'Carro Productos'
        ordering = ['id'] 

    @property
    def order(self):
        return self.orders.first()

class ProductInBox(models.Model):
    product_box = models.ForeignKey(ProductBox, on_delete=models.CASCADE, related_name='product_in_boxes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in_boxes')
    quantity = models.IntegerField(default=1, verbose_name="Cantidad")

    def __str__(self):
        return f"{self.quantity} de {self.product.name}"

@receiver(pre_save, sender=ProductBox)
def set_box_id(sender, instance, *args, **kwargs):
    if not instance.box_id:
        # Generar un ID único para el carrito.
        instance.box_id = str(uuid.uuid4())

@receiver(pre_save, sender=ProductBox)
def update_total(sender, instance, *args, **kwargs):
    if not instance.pk:
        # Si no tiene clave primaria, todavía no se ha guardado en la base de datos
        return
    
    total = sum(product_in_box.product.price * product_in_box.quantity for product_in_box in instance.product_in_boxes.all())
    instance.total = total