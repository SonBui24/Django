from django.contrib import admin

from .models import Employee, Customer, Order, Product, OderDetail


admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OderDetail)
