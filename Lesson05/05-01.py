from sale_management.models import Employee
from random import randint
import names

for i in range(1, 51):
    Employee.objects.create(name=i, address='Hà Nội')


for i in range(50):
    full_name = names.get_full_name()
    first_name = full_name.split(" ", 1)[0]
    Customer.objects.create(name=full_name, address='USA', phone='097' + str(randint(1000000, 9999999)),
                            contact_name=first_name)
