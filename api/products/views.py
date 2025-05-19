from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
