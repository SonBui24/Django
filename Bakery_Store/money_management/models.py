from django.db import models
from Bakery_Store.models import TrackingAbstract, NameAbstractModels


class Category(TrackingAbstract):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Transaction(TrackingAbstract, NameAbstractModels):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    note = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'Name: {self.name} - Amount: {self.amount}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.category.name == 'Expense':
            self.amount = -self.amount
        super(Transaction, self).save(force_insert, force_update, using, update_fields)
