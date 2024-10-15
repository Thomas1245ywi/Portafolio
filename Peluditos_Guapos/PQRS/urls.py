from django.urls import path
from .views import formulario_pqrs, mostrar_pqrs,  editar_pqrs, eliminar_pqrs, generar_reporte_tipos_pqrs, generar_reporte_general_pqrs

urlpatterns = [
    # URL para mostrar el formulario para enviar PQRS
    path('formulario_pqrs/', formulario_pqrs, name='formulario_pqrs'),
    # URL para mostrar las PQRS registradas
    path('mostrar_pqrs/', mostrar_pqrs, name='mostrar_pqrs'),
    # URL para editar una PQRS
    path('editar_pqrs/<int:pqrs_id>/', editar_pqrs, name='editar_pqrs'),
    # URL para eliminar una PQRS
    path('eliminar_pqrs/<int:pqrs_id>/', eliminar_pqrs, name='eliminar_pqrs'),
    # URL para generar el reporte de PQRS
    path('generar_reporte_tipos_pqrs/', generar_reporte_tipos_pqrs, name='generar_reporte_tipos_pqrs'),
    path('generar_reporte_general_pqrs/', generar_reporte_general_pqrs, name='generar_reporte_general_pqrs'),
   
]

