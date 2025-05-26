from django.db.models import Q
from django_filters import rest_framework as filters

from brands.models import Brand


class BrandFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )

    class Meta:
        model = Brand
        fields = {
            'name': ['icontains']
        }
