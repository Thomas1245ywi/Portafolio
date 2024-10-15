from .models import Tipo_pqrs
from collections import Counter

def generar_reporte_tipos_pqrs():
    # Obtener todos los tipos de PQRS
    tipos_pqrs = Tipo_pqrs.objects.all()

    # Contar la cantidad de PQRS para cada tipo
    cantidad_por_tipo = Counter([tipo.Tipo_pqrs for tipo in tipos_pqrs])

    # Ordenar los resultados por la cantidad de PQRS de forma descendente
    tipos_pqrs_mas_repetitivos = sorted(cantidad_por_tipo.items(), key=lambda x: x[1], reverse=True)

    # Imprimir el reporte o guardarlo en un archivo, enviarlo por correo, etc.
    for tipo, cantidad in tipos_pqrs_mas_repetitivos:
        print(f"Tipo de PQRS: {tipo}, Cantidad: {cantidad}")

    # Retorna los tipos de PQRS más repetitivos (opcional)
    return tipos_pqrs_mas_repetitivos
