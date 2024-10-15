import uuid
from django.db import models
from django.db.models.signals import pre_save
from users.models import User
from CarroProductos.models import ProductBox  
from decimal import Decimal

class ProductOrder(models.Model): 
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ForeignKey(ProductBox, on_delete=models.CASCADE, related_name='orders')
    shipping_total = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

    def get_total(self):
        total = Decimal('0.00')
        for product_in_box in self.box.product_in_boxes.all():
            total += product_in_box.product.price * product_in_box.quantity
        return total

    class Meta:
        verbose_name = 'Pedidos Producto'
        verbose_name_plural = 'Pedidos Producto'
        ordering = ['id'] 
    



def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()

pre_save.connect(set_order_id, sender=ProductOrder)
pre_save.connect(set_total, sender=ProductOrder)