from django.contrib import admin

# Register your models here.
from .models import product,Token

@admin.register(product)

class productadmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price')
    list_filter  = ('product_name', 'product_price')

admin.site.register(Token)
