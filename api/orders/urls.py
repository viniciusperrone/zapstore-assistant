from django.urls import path

from orders.views import OrderListCreateAPIView
from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/orders', OrderListCreateAPIView.as_view(), name='order-list-create-api-view')
]
