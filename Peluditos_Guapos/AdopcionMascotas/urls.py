from django.urls import path
from .views import *
from django.contrib.auth.decorators  import login_required


urlpatterns = [

    path('adopcion/', login_required(adopcion_mascotas), name='adopcion'),
    path('reporte-mascotas/', login_required(reporte_mascotas), name='reporte_mascotas'),
    path('detalles-mascota/<slug:slug>', login_required(detalles_mascota.as_view()), name='detalles_mascota'),
]
