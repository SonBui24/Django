from django.db import models
from Bakery_Store.models import TrackingAbstract, NameAbstractModels
from money_management.constants import Class


class Category(TrackingAbstract, NameAbstractModels):
    class_choices = models.IntegerField(default=0, choices=Class.CLASS_CHOICES)

    @property
    def class_choices_str(self):
        return Class.CLASS_CHOICES_DICT.get(self)

    def __str__(self):
        return f'{self.get_class_choices_display()} - {self.name}'


class Transaction(TrackingAbstract, NameAbstractModels):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    note = models.CharField(max_length=1000)

    def __str__(self):
        return f'Name: {self.name} - Amount: {self.amount}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.category.class_choices == 0:
            self.amount = -self.amount
        super(Transaction, self).save(force_insert, force_update, using, update_fields)
