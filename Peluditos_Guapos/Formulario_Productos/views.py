from django.shortcuts import render, redirect
from .forms import Formulario_Productos
from .models import FormularioProducto 
from django.contrib.auth.decorators import login_required

from CarroProductos.utils import get_or_create_product_box
from django.contrib import messages

def formulario_producto(request):
    product_form = Formulario_Productos(request.POST or None)

    if request.method == 'POST' and product_form.is_valid():
        formulario = product_form.save(commit=False)
        formulario.user = request.user
        formulario.save()

        request.session['producto_id'] = formulario.id
        box = get_or_create_product_box(request)
        box.save()

        messages.success(request, '¡Listo! Hemos recibido tu solicitud y estamos trabajando en ello. Pronto nos pondremos en contacto contigo por teléfono para proporcionarte más detalles. ¡Gracias por elegirnos!')
        return redirect('index_real')  # Redirige a la página de historial de compras

    return render(request, 'form_product.html', {'product_form': product_form})


@login_required
def historial_compras(request):
    compras = FormularioProducto.objects.filter(user=request.user).order_by('-fecha_compra')
    return render(request, 'historial_compras.html', {'compras': compras})