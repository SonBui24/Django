from django.urls import path

from sale_management.views import employee, order, product

urlpatterns = [
    path('employee/<int:pk>/', employee.DetailView.as_view(), name='employee_detail'),
    path('employee/', employee.ListingView.as_view(), name='employee_listing'),

    path('order/<int:pk>/', order.DetailView.as_view(), name='order_detail'),
    path('order/', order.ListingView.as_view(), name='order_listing'),
    path('order/<int:order_id>/update_status/', order.update_status, name='update_status'),
    path('order/<int:order_id>/print_order/', order.print_order, name='print_order'),

    path('product/<int:pk>/', product.DetailView.as_view(), name='product_detail'),
    path('product/', product.ListingView.as_view(), name='product_listing'),
    path('product/<int:product_id>/product_update/', product.update_price, name='update_price'),
    path('product/export/', product.export_product, name='export_product'),
]
