from rest_framework import serializers
from .models import Category, Transaction


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['class_choices_str', 'name']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Transaction
        fields = ['category_name', 'amount', 'note']
