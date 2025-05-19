from django.urls import path

from inventory.views import InventoryListCreateAPIView, InventoryRetrieveUpdateDestroyAPIView
from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/inventory/inflow/', InventoryListCreateAPIView.as_view(), name='inflows-list-create-api-view'),
    path(f'{BASIC_API_URL}/inventory/inflow/<int:pk>', InventoryRetrieveUpdateDestroyAPIView.as_view(), name='inflows-detail-api-view'),
]
