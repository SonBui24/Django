"""Bakery_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from bakery_management.views import ProductViewSet, HistoryViewSet, AddQuantityProduct, CloseProduct
from money_management.views import CategoryViewSet, TransactionViewSet, GetAllExpenseView, DetailExpenseView

router = DefaultRouter()
# router.register('list-product', ProductViewSet, basename='list-product')
router.register('history', HistoryViewSet, basename='history')
router.register('category', CategoryViewSet, basename='category')
router.register('transaction', TransactionViewSet, basename='transaction')
# router.register('amount-expense', GetAllExpenseView, basename='amount-expense')

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/list-product/', ProductViewSet.as_view()),
    path('api/add-product/', AddQuantityProduct.as_view(), name="add-product"),
    path('api/close-product/', CloseProduct.as_view(), name="add-product"),
    path('api/amount-expense/', GetAllExpenseView.as_view(), name="amount-expense"),
    path('api/detail-expense/', DetailExpenseView.as_view(), name="detail-expense"),
    path('login/', obtain_auth_token, name='login'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
