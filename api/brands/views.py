from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from brands.models import Brand
from brands.serializers import BrandSerializer


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
