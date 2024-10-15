"""
URL configuration for PeluditosGuapos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import include
from django.contrib.auth.decorators  import login_required




urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', views.index, name='index'),
    path('index_real', login_required(views.index_real), name='index_real'),
    path('accounts/login/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar_sesion/', login_required(views.cerrar_sesion), name='cerrar_sesion'),
    path('registrarme/', views.registrarme, name='registrarme'),
    path('AdopcionMascotas/',include('AdopcionMascotas.urls')),
    path('CajaMascotas/',include('CajaMascotas.urls')),
    path('Productos/',include('Productos.urls')),
    path('PQRS/',include('PQRS.urls')),
    path("DatosAdopcion", include('orders.urls')),


    path('PQRS/',include('PQRS.urls')),
    path('CarroProductos/',include('CarroProductos.urls')),
    path("FormularioAdopcion", include('formulario_adopcion.urls')),
    path("DatosProductos", include('orders_product.urls')),
    path("FormularioProductos", include('Formulario_Productos.urls')),

    
]


"Nos permitira extender las rutas y mostrar las imagenes en nuestro templates"
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)