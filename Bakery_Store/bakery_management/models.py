from Bakery_Store.models import TrackingAbstract, NameAbstractModels
from django.db import models
from bakery_management.constants import HistoryType


class Product(TrackingAbstract, NameAbstractModels):
    price = models.BigIntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Name: {self.name} - Quantity: {self.quantity}'


class History(TrackingAbstract):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    type = models.IntegerField(default=HistoryType.ADD_QUANTITY, choices=HistoryType.HISTORY_CHOICES)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Name: {self.product.name} - Price: {self.price}'

    @property
    def type_str(self):
        return HistoryType.HISTORY_CHOICES_DICT.get(self.type)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.type != 0 and self.product.quantity < self.quantity:
            raise ValueError(
                'Cannot update history because "current quantity" < "expired quantity" or "sold quantity"'
            )

        self.price = self.product.price

        super(History, self).save(force_insert, force_update, using, update_fields)
        if self.type == 0:
            self.product.quantity += self.quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
