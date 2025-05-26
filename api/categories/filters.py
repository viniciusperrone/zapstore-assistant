from django_filters import rest_framework as filters
from django.db.models import Q

from categories.models import Category


class CategoryFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )

    class Meta:
        model = Category
        fields = {
            'name': ['icontains'],
            'description': ['icontains']
        }
