from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
