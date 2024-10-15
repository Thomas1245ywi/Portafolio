# forms.py
from django import forms
from .models import PQRS
from .models import Tipo_pqrs



class FormAgendarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['correo', 'descripcion', 'Tipo_pqrs']

    def __init__(self, *args, **kwargs):
        super(FormAgendarPqrs, self).__init__(*args, **kwargs)
        self.fields['Tipo_pqrs'].empty_label = "Seleccionar"


class FormEditarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['Tipo_pqrs', 'correo', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(FormEditarPqrs, self).__init__(*args, **kwargs)
        self.fields['Tipo_pqrs'].queryset = Tipo_pqrs.objects.all()


class FormEliminarPqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = []  # No se necesitan campos, ya que es solo para confirmar la eliminación

