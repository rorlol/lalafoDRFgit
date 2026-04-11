from .models import Products
from django_filters import filters, FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Products
        fields = {
            'category':['exact'],
            'price':['gt','lt']
        }