from django.shortcuts import render
from .utils import get_or_create_product_order  
from CarroProductos.utils import get_or_create_product_box

def order_product(request):
    box = get_or_create_product_box(request)
    product_order = get_or_create_product_order(box, request)
    
    # Obtener los productos asociados al carrito
    products_in_box = box.products.all()
    
    return render(request, 'order_product.html', {
        'box': box,
        'product_order': product_order,
        'products_in_box': products_in_box  # Pasar los productos al contexto
    })

