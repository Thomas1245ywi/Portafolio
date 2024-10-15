from django.urls import path
from .views import *
app_name ='CajaMascotas'
from django.contrib.auth.decorators  import login_required


urlpatterns = [

    path('', login_required(caja_mascotas), name='caja_mascotas'),
    path('agregar', login_required(add), name='add'),
    path('eliminar', login_required(remove), name='remove'),



]
