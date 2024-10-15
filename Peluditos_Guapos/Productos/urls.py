from django.urls import path
from .views import productos, detalles_productos, confirmacion_compra, ProductosPorCategoriaPDF
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    path('productos/', login_required(productos), name='productos'),
    path('detalles_productos/<int:pk>', login_required(detalles_productos.as_view()), name='detalles_productos'),
    path('confirmacion_compra/', confirmacion_compra, name='confirmacion_compra'),
    path('reporte_productos_por_categoria/', ProductosPorCategoriaPDF.as_view(), name='reporte_productos_por_categoria'),
]