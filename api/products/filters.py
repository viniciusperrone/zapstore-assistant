from django_filters import rest_framework as filters

from products.models import Product


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            'description': ['icontains']
        }
