import io
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from sale_management.models import Order
from django.views import generic
from sale_management.constants import OrderStatus
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


# def detail(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     context = {
#         'order': order,
#         'order_detail_list': order.orderdetail_set.all(),
#     }
#     return render(request, 'sale_management/order/detail.html', context)


class DetailView(generic.DetailView):
    model = Order
    template_name = 'sale_management/order/detail.html'

# def listing(request):
#     order_list = Order.objects.all()
#     context = {
#         'order_list': order_list,
#     }
#     return render(request, 'sale_management/order/index.html', context)


class ListingView(generic.ListView):
    template_name = 'sale_management/order/index.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        return Order.objects.all()


def _previous_status(order):
    message = ''
    pre_status = order.status

    if order.status == OrderStatus.STATUS_ACCEPTED:
        pre_status = OrderStatus.STATUS_NEW
    else:
        message = 'Dont have previous status'

    return pre_status, message


def _next_status(order):
    message = ''
    next_status = order.status

    if order.status == OrderStatus.STATUS_NEW:
        next_status = OrderStatus.STATUS_ACCEPTED
    else:
        message = 'Dont have next status'

    return next_status, message


def update_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if 'previous' in request.POST:
        pre_status, message = _previous_status(order)
        if not message:
            order.status = pre_status
            order.save()
    elif 'next' in request.POST:
        next_status, message = _next_status(order)
        if not message:
            order.status = next_status
            order.save()
    else:
        message = 'Invalid action'

    order = get_object_or_404(Order, pk=order_id)
    return render(
        request,
        'sale_management/order/detail.html',
        {
            'order': order,
            'message': message
        }
    )


def print_detail(request, order_id):
    return render(
        request,
        'sale_management/order/print_detail.html'
    )


def print_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    customer = order.customer
    employee = order.employee
    purchase_at = str(order.purchase_at)
    status = order.status_str

    buffer = io.BytesIO()  # Creat a file buffer
    pdf = canvas.Canvas(buffer)
    pdf.drawCentredString(10.5*cm, 28*cm, f'Customer: {customer.name}')
    pdf.drawCentredString(10.5 * cm, 27 * cm, f'Employee: {employee.name}')
    pdf.drawCentredString(10.5 * cm, 26 * cm, f'Purchase date: {purchase_at}')
    pdf.drawCentredString(10.5 * cm, 25 * cm, f'Status: {status}')
    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='oder')
