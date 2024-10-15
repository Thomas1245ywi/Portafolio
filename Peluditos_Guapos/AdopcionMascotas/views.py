from django.shortcuts import render
from .models import Pet
from CajaMascotas.models import AdoptBox

from django.views.generic.detail import DetailView # esto se usa para obtner los datos de determinado elemento por su id
from django.db.models import Q


# Create your views here.

def adopcion_mascotas(request):

    search_term = request.GET.get('busqueda')
    if search_term:
        # Buscar las mascotas que contienen el término de búsqueda en el nombre o la categoría
        datePet = Pet.objects.filter(Q(name__icontains=search_term) | Q(race__name__icontains=search_term))
    else:
        # Si no hay búsqueda
        datePet = Pet.objects.filter(StatePet__name='No Adoptado').all()
    
    return render(request, 'vistas/adopcion_mascotas.html', {"mascotas": datePet})




class detalles_mascota(DetailView): 
    model = Pet
    template_name = 'vistas/detalles_mascota.html'

def reporte_mascotas(request):
    cajas = AdoptBox.objects.all()
    conteo_mascotas = {}  # Diccionario para realizar un seguimiento de cuántas veces aparece cada tipo de mascota
    
    for caja in cajas:
        for mascota in caja.pets.all():
            tipo_mascota = mascota.type  
            conteo_mascotas[tipo_mascota] = conteo_mascotas.get(tipo_mascota, 0) + 1
    
    # Encontrar el tipo de mascota más común
    tipo_mas_comun = max(conteo_mascotas, key=conteo_mascotas.get)
    cantidad_tipo_mas_comun = conteo_mascotas[tipo_mas_comun]
    
    return render(request, 'vistas/reporte.html', {'cajas': cajas, 'tipo_mas_comun': tipo_mas_comun, 'cantidad_tipo_mas_comun': cantidad_tipo_mas_comun})