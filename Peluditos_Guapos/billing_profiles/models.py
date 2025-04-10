from django.db import models

from users.models import User

class BillingProfile(models.Model):
    user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE, verbose_name="Usuario")
    token = models.CharField(max_length=50, null=False, blank=False)
    card_id = models.CharField(max_length=50, null=False, blank=False,)
    last4= models.CharField(max_length=4, null=False, blank=False)
    brand=models.CharField(max_length=10, null=False, blank=False, )
    default=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.card_id