from django.contrib import admin
from .models import Category, Transaction


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1
    fields = ['name', 'created_at']
    readonly_fields = ['created_at']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Categories', {
            'fields': ['class_choices', 'name']
        })
    ]

    list_display = ['class_choices', 'name']
    list_display_links = ['name']


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transition', {
            'fields': ['name', 'category', 'amount', 'note']
        })
    ]

    list_display = ['category', 'name', 'amount', 'note']
    list_display_links = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)
