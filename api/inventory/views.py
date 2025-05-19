from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from inventory.models import Inflow
from inventory.serializers import InflowSerializer


class InventoryListCreateAPIView(ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InventoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
