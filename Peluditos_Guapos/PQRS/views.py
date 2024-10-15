from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
from django.db.models import Count
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings
from xhtml2pdf import pisa 
from django.utils import timezone




from .models import Tipo_pqrs
from .models import PQRS

from .forms import FormAgendarPqrs

from .forms import FormEditarPqrs  # Importa el formulario de edición


@login_required
def formulario_pqrs(request):
    if request.method == 'POST':
        form = FormAgendarPqrs(request.POST)
        if form.is_valid():
            tipo_pqrs_id = request.POST.get('Tipo_pqrs')
            try:
                tipo_pqrs = Tipo_pqrs.objects.get(pk=tipo_pqrs_id)
                pqrs = form.save(commit=False)
                pqrs.usuario = request.user  # Asociar la PQRS con el usuario actual
                pqrs.Tipo_pqrs = tipo_pqrs
                pqrs.save()
                messages.success(request, 'PQRS enviada exitosamente.')
                form = FormAgendarPqrs()
            except Tipo_pqrs.DoesNotExist:
                messages.error(request, 'El tipo de PQRS seleccionado no existe.')
        else:
            messages.error(request, 'Error al enviar el mensaje. Revise los datos.')

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = FormAgendarPqrs()

    context = {'form': form}
    return render(request, 'vistas/formulario_pqrs.html', context)
def mostrar_formulario(request):
    return render(request, 'vistas/formulario_pqrs.html')


def index(request):
    return render(request, 'vistas/formulario_pqrs.html')

def index_real(request):
    return render(request, 'index_real.html')


@login_required
def mostrar_pqrs(request):
    pqrs_list = PQRS.objects.filter(usuario=request.user)  # Filtrar por el usuario actual
    # Verificar si alguna de las PQRS no tiene respuesta pero sí tiene la opción de editar y eliminar
    mostrar_encabezado_acciones = any(not pqrs.Respuesta for pqrs in pqrs_list)
    context = {'pqrs_list': pqrs_list, 'mostrar_encabezado_acciones': mostrar_encabezado_acciones}
    return render(request, 'vistas/mostrar_pqrs.html', context)


def editar_pqrs(request, pqrs_id):
    pqrs = get_object_or_404(PQRS, pk=pqrs_id)
    
    if request.method == 'POST':
        form = FormEditarPqrs(request.POST, instance=pqrs)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los cambios se guardaron correctamente.')
            return redirect('mostrar_pqrs')
    else:
        form = FormEditarPqrs(instance=pqrs)
    
    context = {'form': form, 'pqrs': pqrs}
    return render(request, 'editar_pqrs.html', context)

def eliminar_pqrs(request, pqrs_id):
    # Obtener la instancia de la PQRS o devolver un error 404 si no existe
    pqrs = get_object_or_404(PQRS, pk=pqrs_id)
    
    # Verificar si la solicitud es POST (es decir, si se envió un formulario)
    if request.method == 'POST':
        # Eliminar la PQRS y redirigir a alguna vista después de la eliminación
        pqrs.delete()
        return redirect('mostrar_pqrs')
    
    # Si la solicitud no es POST, renderizar la plantilla de confirmación de eliminación
    return render(request, 'eliminar_pqrs.html', {'pqrs': pqrs})



def generar_reporte_tipos_pqrs(request):
    # Obtener tipos de PQRS con cantidad
    tipos_pqrs_con_cantidad = Tipo_pqrs.objects.annotate(cantidad_pqrs=Count('pqrs')).order_by('-cantidad_pqrs')

    # Crear un objeto BytesIO para almacenar el PDF generado
    buffer = BytesIO()

    # Crear el documento PDF con un título personalizado
    pdf_title = "Reporte"  # Título personalizado del PDF
    pdf = SimpleDocTemplate(buffer, pagesize=letter, title=pdf_title)
    elements = []

    # Estilo para los párrafos
    styles = getSampleStyleSheet()
    estilo_normal = styles['Normal']

    # Agregar título al PDF
    titulo = Paragraph('Reporte de Tipos de PQRS más repetitivos', estilo_normal)
    elements.append(titulo)
    elements.append(Paragraph('<br/><br/>', estilo_normal))  # Espacio en blanco

    # Crear una tabla a partir de los datos
    data = [['Tipo de PQRS', 'Cantidad de PQRS']]
    for tipo_pqrs in tipos_pqrs_con_cantidad:
        data.append([tipo_pqrs.Tipo_pqrs, tipo_pqrs.cantidad_pqrs])

    # Configurar el estilo de la tabla
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Crear la tabla y aplicar el estilo
    tipos_pqrs_table = Table(data)
    tipos_pqrs_table.setStyle(style)
    elements.append(tipos_pqrs_table)

    # Construir el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y limpiarlo
    pdf_content = buffer.getvalue()
    buffer.close()

    # Crear una respuesta HTTP con el contenido del PDF
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    return response


def generar_reporte_general_pqrs(request):
    pqrs_list = PQRS.objects.all()

    template_path = 'reporte_general_pqrs.html'
    context = {'pqrs_list': pqrs_list}
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="reporte_general_pqrs.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf-8')

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    
    return response


