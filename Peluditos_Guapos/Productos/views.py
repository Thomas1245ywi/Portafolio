from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.db.models import Q
from CarroProductos.utils import get_or_create_product_box
from easy_pdf.views import PDFTemplateView
from django.http import HttpResponse

# Vista para la página de confirmación de compra
def confirmacion_compra(request):
    return render(request, 'vistas/confirmacion_compra.html')

# Vista para la página de listado de productos
@login_required
def productos(request):
    search_term = request.GET.get('q')
    if search_term:
        # Buscar los productos que contienen el término de búsqueda en el nombre o la categoría
        lista_productos = Product.objects.filter(Q(name__icontains=search_term) | Q(category__name__icontains=search_term))
    else:
        # Si no hay búsqueda, se mostrarán todos los productos
        lista_productos = Product.objects.all()
    return render(request, 'vistas/productos.html', {"productos": lista_productos})

# Vista para la página de detalles de un producto
class detalles_productos(DetailView): 
    model = Product
    template_name = 'vistas/detalles_productos.html'
    
    def post(self, request, *args, **kwargs):
        # Manejar la solicitud POST para agregar el producto al carrito
        product = self.get_object()
        box = get_or_create_product_box(request)
        box.products.add(product)
        return redirect('CarroProductos:caja_productos')

class ProductosPorCategoriaPDF(PDFTemplateView):
    template_name = "productos_por_categoria_pdf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todas las categorías
        categorias = Category.objects.all()
        # Crear un diccionario para almacenar productos por categoría
        productos_por_categoria = {}
        for categoria in categorias:
            # Filtrar productos por categoría y almacenar en el diccionario
            productos_por_categoria[categoria.name] = Product.objects.filter(category=categoria)
        context['productos_por_categoria'] = productos_por_categoria
        return context
