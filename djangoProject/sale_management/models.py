from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True)  # date of birth

    def __str__(self):
        return f'{self.id} - {self.name}'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.phone}'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_at = models.DateTimeField()
    delivery_at = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} - {self.purchase_at} - {self.delivery_at}'


class OderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.quantity}'
