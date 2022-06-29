from Bakery_Store.models import TrackingAbstract, NameAbstractModels
from django.db import models
from bakery_management.constants import HistoryType
from django.core.exceptions import ValidationError


class Product(TrackingAbstract, NameAbstractModels):
    price = models.BigIntegerField()
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Name: {self.name} - Quantity: {self.quantity}'


class History(TrackingAbstract):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    type = models.IntegerField(default=HistoryType.ADD_QUANTITY, choices=HistoryType.HISTORY_CHOICES)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self):
        return f'Name: {self.product.name} - Price: {self.price}'

    @property
    def type_str(self):
        return HistoryType.HISTORY_CHOICES_DICT.get(self.type)

    def product_name(self):
        return self.product.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.price = self.product.price

        super(History, self).save(force_insert, force_update, using, update_fields)
        if self.type == HistoryType.ADD_QUANTITY:
            self.product.quantity += self.quantity

        elif self.type == HistoryType.EXPIRED_QUANTITY:
            if self.product.quantity < self.quantity:
                raise ValidationError(
                    'Cannot update history because "current quantity" < "expired quantity"'
                )
            else:
                self.product.quantity -= self.quantity

        else:
            if self.product.quantity < self.quantity:
                raise ValidationError(
                    'Cannot update history because "current quantity" > "inventory quantity"'
                )
            else:
                self.product.quantity = self.quantity
        self.product.save()
