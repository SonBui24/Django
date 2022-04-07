from sale_management.models import Employee
for i in range(1, 51):
    Employee.objects.create(name=i, address='Hà Nội')
