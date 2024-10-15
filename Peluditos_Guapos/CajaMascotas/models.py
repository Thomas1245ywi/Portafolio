import uuid #esto nos ayuda a crear keys algo mas complejas
from django.db import models
from users.models import User
from AdopcionMascotas.models import Pet
from django.db.models.signals import pre_save




class StateBox(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nombre')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado Caja' # Cuando se registre la BD en Django
        verbose_name_plural = 'Estados Cajas'
        db_table = 'Estado Caja' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente


class AdoptBox(models.Model):

    #----------Atento para algunas corerciones-------------------------
    #creamos primary key segura para no exponer el sistema(security)
    box_id = models.CharField(max_length=100, null=False,blank=False,unique=True) 
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuario") #Uno a muchos
    pets = models.ManyToManyField(Pet) #Muchos a Muchos
    #suma del precio mas todos sus productos
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name="Sub Total")#2 digitos despues del punto decimal
    #suma del subtotal mas una comision
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, verbose_name="Total")#2 digitos despues del punto decimal
    create_at = models.DateTimeField(auto_now_add=True)
    StateBox = models.ForeignKey(StateBox, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Estado')


    def __str__(self):
        return self.box_id + "-" + self.user.username
    
    class Meta:
        verbose_name = 'Caja Adopcion' # Cuando se registre la BD en Django
        verbose_name_plural = 'Cajas Adopciones'
        db_table = 'Caja Adopcion' # Nombre de la tabla
        ordering = ['id'] # Orden ascendente
    
    @property
    def order(self):
        return self.order_set.first()
    
    

    

def set_box_id(sender,instance, *args, **kwargs):
    if not instance.box_id:
        #este metodo nos genera keys
        instance.box_id = str(uuid.uuid4())

pre_save.connect(set_box_id,sender=AdoptBox)