from django.contrib import admin
from .models import Tipo_pqrs, Estado, PQRS
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import format_html
# Register your models here.

#Aqui le decimos que campos queremos que se exporten cuando le demos exportar
class PQRSResource(resources.ModelResource):
    class Meta:
        model = PQRS
        fields = ('id','Tipo_pqrs', 'correo', 'descripcion', 'Estado','Respuesta')

@admin.register(PQRS)
class PQRSAdmin(ImportExportModelAdmin):
    resource_class = PQRSResource
    list_display = ('correo', 'descripcion', 'generate_report_link')  # Agrega el método generate_report_link a list_display
    list_display_links = ('correo',)
    list_editable = ('descripcion',)
    list_filter = ('correo', 'Tipo_pqrs',)
    list_per_page = 6
    

    def generate_report_link(self, obj):
        report_url = reverse('generar_reporte_general_pqrs')  # Reemplaza 'generar_reporte_general_pqrs' con el nombre de tu URL para generar el reporte general
        return format_html('<a href="{}">Generar Reporte General</a>', report_url)
    generate_report_link.short_description = 'Generar Reporte'


    
class TipoPQRSAdmin(admin.ModelAdmin):
    list_display = ['Tipo_pqrs']
    actions = ['generar_reporte']

    def generar_reporte(self, request, queryset):
        # Redirige a la URL del PDF
        return HttpResponseRedirect(reverse('generar_reporte_tipos_pqrs'))

    # Define un nombre más descriptivo para la acción
    generar_reporte.short_description = 'Generar Reporte PDF'


admin.site.register(Tipo_pqrs, TipoPQRSAdmin)
admin.site.register(Estado)
