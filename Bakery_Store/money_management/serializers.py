from rest_framework import serializers
from .models import Category, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class WriteTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'category',
            'name',
            'amount',
            'note'
        ]


class ReadTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'id',
            'category',
            'name',
            'amount',
            'note'
        ]

        read_only_fields = fields


class GetAllExpenseSerializer(serializers.Serializer):
    total_expense = serializers.IntegerField()
    created_at__date = serializers.DateField()


class DetailExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name', 'amount']
