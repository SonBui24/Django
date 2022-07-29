from rest_framework import serializers
from bakery_management.models import Product, History


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']


class AddQuantityProductSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    add_quantity = serializers.IntegerField()


class ListAddQuantityProductSerializer(serializers.Serializer):
    items = AddQuantityProductSerializer(many=True)


class CloseProductSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    expired_quantity = serializers.IntegerField()
    inventory_quantity = serializers.IntegerField()


class ListCloseProductSerializer(serializers.Serializer):
    items = CloseProductSerializer(many=True)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'product_name', 'type_str', 'quantity', 'price']

