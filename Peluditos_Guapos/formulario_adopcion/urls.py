from django.urls import path
from . import views
from django.contrib.auth.decorators  import login_required



app_name = 'formulario_adopcion'

urlpatterns = [
    path('',login_required(views.form_adoption),name='formularioAdopcion'),
    path('detalles', login_required(views.details_adoption), name='details')
]
