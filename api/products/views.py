from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters

from products.models import Product
from products.serializers import ProductSerializer
from products.filters import ProductFilter


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
