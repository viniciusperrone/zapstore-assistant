from rest_framework.generics import ListCreateAPIView

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
