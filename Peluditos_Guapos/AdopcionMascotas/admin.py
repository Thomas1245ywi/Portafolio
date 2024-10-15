from django.contrib import admin
from .models import Pet, StatePet, Type, Race
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    fields = ('plate','name', 'age', 'description_short', 'description', 'type', 'race','StatePet','photo')
    list_display = ('plate','name','race', 'report_button')
    list_display_links = ('plate', 'name')
    list_filter = ('race',)
    list_per_page = 10

    def report_button(self, obj):
        url = reverse('reporte_mascotas')  # Reemplaza 'reporte_mascotas' con la URL de tu reporte
        return format_html('<a class="btn btn-primary" href="{}">Generar Reporte</a>', url)

    report_button.short_description = 'Reporte'  # Texto para mostrar en la columna
# Register your models here.


#aqui le decimos que campos queremos que se expoten cuando le demos exportar
class PetResource(resources.ModelResource):
    class Meta:
        model = Pet
        fields = ('id','plate', 'name' ,'age' ,'description_short', 'description' ,'type', 'race', 'StatePet','photo')
    
class RaceResource(resources.ModelResource):
    class Meta:
        model = Race
        fields = ('id','name')

class StateResource(resources.ModelResource):
    class Meta:
        model = StatePet
        fields = ('id','name')

class TypeResource(resources.ModelResource):
    class Meta:
        model = Type
        fields = ('id','name')
    




@admin.register(Race)
class RaceAdmin(ImportExportModelAdmin):
    resource_class = RaceResource


@admin.register(StatePet)
class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource

@admin.register(Type)
class StateAdmin(ImportExportModelAdmin):
    resource_class = TypeResource


