from django.contrib import admin
from .models import Product, Category, ProductType, Brand
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from django.http import HttpResponse
import io

# Register your models here.

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'category', 'product_type', 'brand', 'name', 'price', 'description', 'photo', 'quantity')

@admin.register(Product)
class CustomProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('name', 'price', 'category')
    list_display_links = ('name',)
    list_editable = ('price',)
    search_fields = ('name',)
    list_filter = ('category__name',)
    list_per_page = 8

    def reporte_producto_mas_vendido(self, request, queryset):
        # Obtener el producto más vendido
        producto_mas_vendido = Product.objects.order_by('-cantidad_vendida').first()

        # Crear un buffer de memoria para almacenar el PDF
        buffer = io.BytesIO()

        # Crear un documento PDF
        pdf = canvas.Canvas(buffer, pagesize=letter)
        
        # Definir estilos para el texto
        estilos = getSampleStyleSheet()
        estilo_titulo = estilos['Title']
        estilo_normal = estilos['Normal']

        # Agregar título al documento
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(100, 750, 'Reporte de Producto Más Vendido')

        # Agregar detalles del producto más vendido
        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 720, f'Producto Más Vendido: {producto_mas_vendido.name}')
        pdf.drawString(100, 700, f'Cantidad Vendida: {producto_mas_vendido.cantidad_vendida}')
        pdf.drawString(100, 680, f'Categoría: {producto_mas_vendido.category.name}')
        
        # Agregar descripción del producto en párrafos
        descripcion = producto_mas_vendido.description
        descripcion_paragraphs = descripcion.split("\n")
        y_position = 660
        for paragraph in descripcion_paragraphs:
            pdf.drawString(100, y_position, f'Descripción: {paragraph}')
            y_position -= 20  # Espacio entre párrafos

        # Guardar el PDF
        pdf.showPage()
        pdf.save()

        # Devolver el PDF como una respuesta HTTP
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_producto_mas_vendido.pdf"'
        return response

    reporte_producto_mas_vendido.short_description = 'Generar Reporte del Producto Más Vendido'

    # Agregar el método a la lista de acciones
    actions = ['reporte_producto_mas_vendido']

admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Brand)
