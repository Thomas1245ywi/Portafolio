from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'CarroProductos' 

urlpatterns = [
    path('', login_required(caja_productos), name='caja_productos'),
    path('add_product', login_required(addd), name='addd'),
    path('remove_product', login_required(removee), name='removee'),
]
