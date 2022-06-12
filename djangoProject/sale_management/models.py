from django.db import models
from django.contrib.auth.models import User
from sale_management.constants import OrderStatus, Gender


class CreatedAbstractModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_by',
    )
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modified_by',
    )
    modified_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True
    )

    class Meta:
        abstract = True


class TrackingAbstract(CreatedAbstractModel, ModifiedAbstractModel):
    class Meta:
        abstract = True


class Employee(TrackingAbstract):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True)  # date of birth
    gender = models.IntegerField(default=Gender.UNKNOWN, choices=Gender.GENDER_CHOICES)

    def __str__(self):
        return f'ID: {self.id} - Name: {self.name}'

    def get_gender_display(self):
        gender_dict = dict(Gender.GENDER_CHOICES)
        return gender_dict.get(self.gender)


class Customer(TrackingAbstract):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.phone}'


class Product(TrackingAbstract):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'


class Order(TrackingAbstract):
    id = models.AutoField(primary_key=True)
    purchase_at = models.DateTimeField()
    delivery_at = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=OrderStatus.STATUS_NEW, choices=OrderStatus.STATUS_CHOICES)

    def __str__(self):
        return f'{self.id} - Employee: {self.employee.name} - Customer: {self.customer.name}'

    @property
    def status_str(self):
        return OrderStatus.STATUS_CHOICES_DICT.get(self.status)


class OrderDetail(TrackingAbstract):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.order} - {self.product}'

    @property
    def subtotal(self):
        return self.quantity * self.price
