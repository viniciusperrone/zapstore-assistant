from django.urls import path

from customers.views import CustomerListCreateAPIView
from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/customer', CustomerListCreateAPIView.as_view(), name='customer-list-create-api-view')
]
