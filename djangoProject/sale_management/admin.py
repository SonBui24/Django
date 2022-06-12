from django.contrib import admin
from django.utils import timezone
from .models import Employee, Customer, Order, Product, OrderDetail


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1
    fields = ['product', 'quantity', 'price']


class OrderAdmin(admin.ModelAdmin):
    # fields = ['customer', 'employee', 'status', 'purchase_at', 'delivery_at']
    fieldsets = [
        ('Customer, Employee Information', {
            'fields': ['customer', 'employee']
        }),
        ('Status', {
            'fields': ['status']
        }),
        ('Date Information', {
            'fields': ['purchase_at', 'delivery_at']
        })
    ]

    list_display = ['id', 'customer', 'employee', 'status', 'purchase_at', 'total', 'was_delivered']
    list_display_links = ['id', 'customer', 'employee']

    inlines = [OrderDetailInline]

    def total(self, obj):
        total = 0
        for order_detail in obj.orderdetail_set.all():
            total += order_detail.subtotal
        return total

    def was_delivered(self, obj):
        time_now = timezone.now()
        return obj.delivery_at < time_now
    was_delivered.boolean = True


class OrderDetailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Customer, Employee Information', {
            'fields': ['order']
        }),
        ('Product Information', {
            'fields': ['product', 'quantity', 'price']
        }),
    ]

    list_display = ['id', 'product', 'quantity', 'price', 'subtotal']
    list_display_links = ['id', 'product', 'quantity', 'price']


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['name', 'address', 'dob']
        }),
    ]

    list_display = ['id', 'name', 'address']
    list_display_links = ['id', 'name', 'address']


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['name', 'contact_name', 'address', 'phone']
        }),
    ]

    list_display = ['id', 'name', 'address', 'phone']
    list_display_links = ['id', 'name', 'address', 'phone']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['name', 'quantity', 'price']
        }),
    ]

    list_display = ['id', 'name', 'quantity', 'price', 'total_inventory_price']
    list_display_links = ['id', 'name', 'quantity', 'price']

    def total_inventory_price(self, obj):
        return obj.price * obj.quantity


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)



