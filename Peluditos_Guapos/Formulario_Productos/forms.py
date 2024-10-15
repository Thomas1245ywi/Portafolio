from django.forms import ModelForm
from .models import FormularioProducto

class Formulario_Productos(ModelForm):
    class Meta:
        model = FormularioProducto
        fields = [
            'full_name', 'phone', 'address', 'city', 'neighborhood'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['phone'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['address'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['city'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['neighborhood'].widget.attrs.update({
            'class': 'form-control'
        })
