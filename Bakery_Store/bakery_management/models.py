from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.BigIntegerField()
    quantity = models.IntegerField()
    expiry = models.DateField(null=True)

    def __str__(self):
        return f'Name: {self.name} - Quantity: {self.quantity} - Expiry: {self.expiry}'


class History(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory_quantity = models.IntegerField(null=False)
    add_quantity = models.IntegerField(null=True)
    price = models.IntegerField()
    date_of_manufacture = models.DateField(null=False)

    def __str__(self):
        return f'Name: {self.product.name} - Inventory_quantity: {self.inventory_quantity} - Price: {self.price}'
