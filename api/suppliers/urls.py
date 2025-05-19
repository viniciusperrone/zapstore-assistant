from django.urls import path

from suppliers.views import SupplierListCreateAPIView, SupplierRetrieveUpdateDestroyAPIView
from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/supplier', SupplierListCreateAPIView.as_view(), name='supplier-list-create-api-view'),
    path(f'{BASIC_API_URL}/supplier/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail-api-view')
]
