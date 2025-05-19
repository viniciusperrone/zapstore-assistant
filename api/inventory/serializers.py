from rest_framework import serializers

from inventory.models import Inflow
from products.serializers import ProductSerializer
from suppliers.serializers import SupplierSerializer


class InflowSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Inflow
        fields = '__all__'
