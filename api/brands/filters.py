from django_filters import rest_framework as filters

from brands.models import Brand


class BrandFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Brand
        fields = ['name']
