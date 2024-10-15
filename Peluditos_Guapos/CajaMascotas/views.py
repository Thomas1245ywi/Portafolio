from django.shortcuts import render
from .models import AdoptBox  
from AdopcionMascotas.models import Pet  
from django.shortcuts import redirect

from .utils import get_or_create_box

# Create your views here.



def caja_mascotas(request):
    
    box = get_or_create_box(request)
    box_state = box.StateBox.name

    
    return render(request, 'caja_mascotas.html',{
        'box' : box,
        'box_state': box_state

    })


def add(request):
    box = get_or_create_box(request)

    #obtenemos las mascotas enviadas por el metodo Post
    pet = Pet.objects.get(pk=request.POST.get('pet_id'))
    


    #Agregamos mascota a carrito
    

    if box.pets.filter(id = pet.pk).exists():
        message = 'La mascota ya se encuentra en la caja'


    else:
        box.pets.add(pet)
        message = 'La mascota ha sido añadida a la caja de Adopcion'


    return render(request, 'add.html',{
        'pet': pet,
        'message':message
    })

def remove(request):
    box = get_or_create_box(request)
    pet = Pet.objects.get(pk=request.POST.get('pet_id'))

    box.pets.remove(pet)

    return redirect('CajaMascotas:caja_mascotas')



