from rest_framework import viewsets, generics, views
from bakery_management.models import Product, History
from .serializers import ProductSerializer, HistorySerializer, AddQuantityProductSerializer, \
    ListAddQuantityProductSerializer, CloseProductSerializer, ListCloseProductSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from .constants import HistoryType


class ProductViewSet(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddQuantityProduct(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request_data = ListAddQuantityProductSerializer(data=request.data)
        if request_data.is_valid():
            items = request_data.data['items']
            for item in items:
                product_id = item['product_id']
                add_quantity = item['add_quantity']
                History.objects.create(product_id=product_id,
                                       price=Product.objects.get(id=product_id).price,
                                       type=0,
                                       quantity=add_quantity)
            return Response('Add success!', status=status.HTTP_200_OK)
        else:
            return Response('Wrong data!', status=status.HTTP_400_BAD_REQUEST)


class CloseProduct(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request_data = ListCloseProductSerializer(data=request.data)
        if not request_data.is_valid():
            return Response('Wrong data', status=status.HTTP_400_BAD_REQUEST)

        items = request_data.data['items']

        for item in items:
            product_id = item['product_id']
            expired_quantity = item['expired_quantity']
            inventory_quantity = item['inventory_quantity']

            History.objects.create(product_id=product_id,
                                   price=Product.objects.get(id=product_id).price,
                                   type=HistoryType.EXPIRED_QUANTITY,
                                   quantity=expired_quantity
                                   )

            History.objects.create(product_id=product_id,
                                   price=Product.objects.get(id=product_id).price,
                                   type=HistoryType.INVENTORY_QUANTITY,
                                   quantity=inventory_quantity
                                   )

        return Response('Success!', status=status.HTTP_200_OK)


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
