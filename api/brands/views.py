from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters

from brands.models import Brand
from brands.serializers import BrandSerializer
from brands.filters import BrandFilter


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandFilter


class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
