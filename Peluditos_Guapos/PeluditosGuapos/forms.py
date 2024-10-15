from typing import Any
from django import forms

from django.contrib.auth.models import User


#por medio de widget podemos aplicar ids y estilos
class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario',
                               required=True,
                               min_length=4, max_length=50, 
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username'

                               }))
    email = forms.EmailField(label='Correo Electronico',
                               required=True,
                               widget=forms.EmailInput(attrs={
                                   'class': 'form-control',
                                   'id': 'email',
                                   

                                   
                               }))
    
    password = forms.CharField(label='Contraseña',
                                required=True,
                                min_length=7,
                                widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                }))
    
    password2 = forms.CharField(label='Confirmar Contraseña',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                }))
    
    

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Este usuario ya se encuentra en uso')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Este correo ya se encuentra en uso')
        return email
    
    #clean se usa si un campo depende de otro
    def clean(self):

        #cleaned data recibe la informacion del formulario lo que nos permite luego comparalos
        cleaned_data =  super().clean()
    
        #cleaned es un diccionario
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','Las contraseñas deben ser iguales')

    def save(self):
        
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),


            )
        



