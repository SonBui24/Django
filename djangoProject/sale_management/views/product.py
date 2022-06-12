from sale_management.models import Product
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
import csv


class DetailView(generic.DetailView):
    model = Product
    template_name = 'sale_management/product/detail.html'


class ListingView(generic.ListView):
    template_name = 'sale_management/product/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


def update_price(request, product_id):
    try:
        price = float(request.POST['price'])
        affected_rows = Product.objects.filter(id=product_id).filter(~Q(price=price)).update(price=price)
        if affected_rows == 1:
            message = 'Update is success'
        else:
            message = 'Price is not changed'
        product = get_object_or_404(Product, pk=product_id)
    except(KeyError, ValueError):
        message = 'Something went wrong!'
    return render(request, 'sale_management/product/detail.html',
        {
            'product': product,
            'message': message,
        }
    )


def export_product(request):
    products = Product.objects.all()

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="products.csv"'}
    )

    writer = csv.writer(response)
    writer.writerow(['Name', 'Price', 'Quantity'])  # header of csv-file
    for product in products:
        writer.writerow([product.name, str(product.price), str(product.quantity)])

    return response
