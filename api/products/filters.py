from django_filters import rest_framework as filters
from django.db.models import Q

from products.models import Product


class ProductFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(description__icontains=value)
        )

    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'brand__name': ['icontains'],
            'category__name': ['icontains'],
        }
