from django.contrib import admin
from .models import Category, Transition


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {
            'fields': ['name']
        })
    ]

    list_display = ['name']
    list_display_links = ['name']


class TransitionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Transition', {
            'fields': ['name', 'category', 'amount', 'note']
        })
    ]

    list_display = ['name', 'amount']
    list_display_links = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Transition, TransitionAdmin)
