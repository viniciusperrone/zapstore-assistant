from rest_framework.generics import ListCreateAPIView

from brands.models import Brand
from brands.serializers import BrandSerializer


class BrandListCreateAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
