from django.shortcuts import render, redirect
from .models import ProductBox, ProductInBox
from Productos.models import Product
from .utils import get_or_create_product_box

def caja_productos(request):
    box = get_or_create_product_box(request)
    
    return render(request, 'caja_productos.html', {
        'box': box
    })

def addd(request):
    box = get_or_create_product_box(request)

    # Obtener el producto enviado por el método POST
    product = Product.objects.get(pk=request.POST.get('product_id'))

    # Obtener la cantidad del producto (si se proporciona)
    quantity = int(request.POST.get('quantity', 1))

    # Verificar si el producto ya está en el carrito
    product_in_box, created = ProductInBox.objects.get_or_create(product_box=box, product=product)

    # Si el producto ya está en el carrito, simplemente actualizar la cantidad
    if not created:
        product_in_box.quantity += quantity
    else:
        product_in_box.quantity = quantity
    
    product_in_box.save()

    return redirect('CarroProductos:caja_productos')

def removee(request):
    box = get_or_create_product_box(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    # Eliminar el producto del carrito
    try:
        product_in_box = ProductInBox.objects.get(product_box=box, product=product)
        product_in_box.delete()
    except ProductInBox.DoesNotExist:
        pass

    return redirect('CarroProductos:caja_productos')
