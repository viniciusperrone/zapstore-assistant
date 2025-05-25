from django_filters import rest_framework as filters

from products.models import Product


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    brand = filters.CharFilter(field_name='brand__name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')


    class Meta:
        model = Product
        fields = ['title', 'description', 'brand', 'category']
