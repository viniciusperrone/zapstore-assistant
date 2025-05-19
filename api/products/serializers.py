from rest_framework import serializers

from products.models import Product
from brands.serializers import BrandSerializer
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'serie_number', 'cost_price', 'selling_price', 'brand', 'category', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
