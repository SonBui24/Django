from sale_management.models import Employee, Customer

em = Employee.objects.last()
cu = Customer.objects.last()

em.address = 'HCM'
em.save()
