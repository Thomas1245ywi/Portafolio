from django.urls import path
from . import views

app_name = 'orders_product'  

urlpatterns = [
    path('', views.order_product, name='orderss'),  
]
