from rest_framework import serializers
from bakery_management.models import Product, History


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['product_name', 'type_str', 'quantity', 'price']

