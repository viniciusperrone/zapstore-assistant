from rest_framework import serializers

from sales.models import Sales
from products.serializers import ProductSerializer


class SalesSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Sales
        fields = '__all__'
