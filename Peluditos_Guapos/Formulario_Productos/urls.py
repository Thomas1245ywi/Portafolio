from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'Formulario_Productos'

urlpatterns = [
    path('', login_required(views.formulario_producto), name='formulario_producto'),
    path('historial-compras/', login_required(views.historial_compras), name='historial_compras'),
]
