from django.db.models import Count
from .models import Pet

def reporte_mascota_mas_solicitada():
    # Calcular cuántas veces aparece cada mascota en todas las cajas de adopción
    mascotas_con_cantidad_de_cajas = Pet.objects.annotate(total_cajas=Count('adopt_box')).order_by('-total_cajas')

    # Determinar la mascota más solicitada
    if mascotas_con_cantidad_de_cajas:
        mascota_mas_solicitada = mascotas_con_cantidad_de_cajas[0]
        total_cajas_mascota_mas_solicitada = mascota_mas_solicitada.total_cajas
    else:
        # Manejar el caso en que no haya mascotas registradas
        mascota_mas_solicitada = None
        total_cajas_mascota_mas_solicitada = 0

    return mascota_mas_solicitada, total_cajas_mascota_mas_solicitada