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


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('History', {
            'fields': ['product', 'add_quantity', 'inventory_quantity', 'price', 'date_of_manufacture']
        })
    ]

    list_display = ['product', 'inventory_quantity', 'price', 'date_of_manufacture']
    list_display_links = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)
