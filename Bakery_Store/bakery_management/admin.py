from django.contrib import admin
from .models import Product, History


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Information', {
            'fields': ['name', 'price', 'quantity', 'expiry']
        })
    ]

    list_display = ['name', 'quantity']
    list_display_links = ['name', 'quantity']


admin.site.register(Product, ProductAdmin)
