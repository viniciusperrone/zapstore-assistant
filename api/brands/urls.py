from django.urls import path

from utils.api import BASIC_API_URL
from brands.views import BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(f'{BASIC_API_URL}/brand', BrandListCreateAPIView.as_view(), name='brand-create-list-api-view'),
    path(f'{BASIC_API_URL}/brand/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-detail-api-view'),
]
