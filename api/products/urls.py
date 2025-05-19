from django.urls import path

from products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/product', ProductListCreateAPIView.as_view(), name='product-list-create-api-view'),
    path(f'{BASIC_API_URL}/product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-list-create-api-view'),
]
