from django.shortcuts import render
from .utils import get_or_create_order
from  CajaMascotas.utils import get_or_create_box


# Create your views here.

def order(request):
    box = get_or_create_box(request)
    order = get_or_create_order(box, request)
    return render(request, 'order.html',{
        'box' : box,
        'order': order
    })
