from sale_management.models import Employee
from django.shortcuts import render, get_object_or_404
from django.views import generic


# def detail(request, employee_id):
#     employee = get_object_or_404(Employee, pk=employee_id)
#     return render(request, 'sale_management/employee/detail.html', {'employee': employee})


class DetailView(generic.DetailView):
    model = Employee
    template_name = 'sale_management/employee/detail.html'


# def listing(request):
#     latest_employee_list = Employee.objects.order_by('-created_at')
#     context = {
#         'latest_employee_list': latest_employee_list,
#     }
#     return render(request, 'sale_management/employee/index.html', context)

class ListingView(generic.ListView):
    template_name = 'sale_management/employee/index.html'
    context_object_name = 'latest_employee_list'

    def get_queryset(self):
        return Employee.objects.order_by('created_at')

