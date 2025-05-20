from rest_framework.generics import ListCreateAPIView

from sales.models import Sales
from sales.serializers import SalesSerializer


class SalesListCreateAPIView(ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
