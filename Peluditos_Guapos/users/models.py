from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(User):
    class Meta:
        proxy = True

      
