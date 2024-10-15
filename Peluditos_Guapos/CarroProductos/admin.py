from django.contrib import admin
from .models import ProductBox

class ProductBoxAdmin(admin.ModelAdmin):
    list_display = ('box_id', 'user', 'subtotal', 'total', 'created_at', )
    list_filter = ('created_at', )
    search_fields = ['box_id', 'user__username']

admin.site.register(ProductBox, ProductBoxAdmin)
