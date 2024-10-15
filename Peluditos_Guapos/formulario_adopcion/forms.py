from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import  ModelForm
from django.forms.utils import ErrorList
from .models import form_adoption
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

class FormAdoptionForm(forms.ModelForm):

    MAX_FILE_SIZE_MB = 5  # Tamaño máximo del archivo en MB

    class Meta:
        model = form_adoption
        fields = ['full_name', 'documentFront','documentBack', 'age', 'direction', 'city', 'neighborhood', 'phone', 'why','work', 'capacityMoney','time','visits','disposition']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'documentFront': forms.FileInput(attrs={'class': 'form-control'}),
            'documentBack': forms.FileInput(attrs={'class': 'form-control'}),            
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'why': forms.Textarea(attrs={'class': 'form-control'}),
            'work': forms.Textarea(attrs={'class': 'form-control'}),
            'capacityMoney': forms.Textarea(attrs={'class': 'form-control'}),
            'time': forms.Textarea(attrs={'class': 'form-control'}),
            'visits': forms.Textarea(attrs={'class': 'form-control'}),
            'disposition': forms.Textarea(attrs={'class': 'form-control'}),

            




            
           

        }

    def limpiar_imagen(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > self.MAX_FILE_SIZE_MB * 1024 * 1024:
                raise ValidationError(_('El tamaño del archivo excede el límite de %s MB.') % self.MAX_FILE_SIZE_MB)
        return image