from CarroProductos.utils import get_or_create_product_box
from .models import ProductOrder  

def get_or_create_product_order(box, request):
    product_order = box.order  # propiedad @property definida

    if product_order is None and request.user.is_authenticated:
        # Crear un nuevo objeto ProductOrder utilizando la información del carrito
        total = box.total  # Obtener el total del carrito
        shipping_total = 0.0  # Definir el costo de envío (si es necesario)
        user = request.user  # Obtener el usuario actual
        
        # Crear el objeto ProductOrder
        product_order = ProductOrder.objects.create(box=box, user=user, shipping_total=shipping_total, total=total)

        # Establecer el ID del objeto ProductOrder en la sesión
        request.session['product_order_id'] = product_order.order_id

    return product_order
