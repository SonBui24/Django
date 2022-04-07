from django.urls import path

from sale_management.views import index, new, cafe

urlpatterns = [
    path('', index, name='index'),
    path('new', new, name='new'),
    path('cafe', cafe, name='cafe')
]
