from django_filters import rest_framework as filters

from brands.models import Brand


class BrandFilter(filters.FilterSet):

    class Meta:
        model = Brand
        fields = {
            'name': ['icontains']
        }
