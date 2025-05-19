from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


class SupplierListCreateAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
