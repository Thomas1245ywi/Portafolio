import uuid
from django.db import models
from enum import Enum
from users.models import User
from CajaMascotas.models import AdoptBox
from django.db.models.signals import pre_save

# Create your models here.

class OrderStatus(Enum):
    CREADO = 'CREADO'
    SOLICITADO = 'SOLICITADO'
    ADOPTADO = 'ADOPTADO'
    COMPLETADO = 'COMPLETADO'
    CANCELADO = 'CANCELADO'

choices = [(tag, tag.value) for tag in OrderStatus]


class Order(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box =  models.ForeignKey(AdoptBox, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=choices, default=OrderStatus.CREADO)
    shipping_total = models.DecimalField(default= 0.00, max_digits= 8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.order_id
    
    def get_total(self):
        return self.shipping_total
    
def set_order_id(sender, instance, *args, **kwargs):

    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()

pre_save.connect(set_order_id, sender= Order)
pre_save.connect(set_total, sender=Order)

    


