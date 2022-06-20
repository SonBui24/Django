from django.contrib import admin
from .models import Product, History


class HistoryInLine(admin.TabularInline):
    model = History
    extra = 1
    fields = ['type', 'quantity', 'price', 'created_at']
    readonly_fields = ['created_at', 'price']
    ordering = ['-created_at']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Information', {
            'fields': ['name', 'price', 'quantity']
        })
    ]
    readonly_fields = ['quantity']
    list_display = ['name', 'quantity']
    list_display_links = ['name', 'quantity']

    inlines = [HistoryInLine]


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('History', {
            'fields': ['product', 'type', 'quantity', 'price']
        })
    ]

    list_display = ['product', 'price', 'created_at']
    list_display_links = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)
