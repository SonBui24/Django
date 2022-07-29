from django.db.models import Sum
from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from money_management.models import Category, Transaction
from .serializers import CategorySerializer, WriteTransactionSerializer, ReadTransactionSerializer, \
    GetAllExpenseSerializer, DetailExpenseSerializer
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

class GetAllExpenseView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = GetAllExpenseSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            amount__lt=0
        ).values('created_at__date').annotate(total_expense=Sum('amount')).values('created_at__date', 'total_expense')


class DetailExpenseView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DetailExpenseSerializer

    def get_queryset(self):
        date = self.request.data['created_at__date']
        return Transaction.objects.filter(created_at__date=date, amount__lt=0)

