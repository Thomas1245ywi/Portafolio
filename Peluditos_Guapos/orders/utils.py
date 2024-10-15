from  CajaMascotas.utils import get_or_create_box
from .models import Order


def get_or_create_order(box, request):

    order = box.order

    if order is None and request.user.is_authenticated :
        order = Order.objects.create(box = box, user = request.user)

    if order:
        
        request.session['order_id'] = order.order_id

    return order
 
