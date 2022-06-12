from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return f'Name: {self.name}'


class Transition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    note = models.CharField(max_length=1000)

    def __str__(self):
        return f'Name: {self.name} - Amount: {self.amount}'
