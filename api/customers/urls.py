from django.urls import path

from customers.views import CustomerListCreateAPIView
from utils.api import CustomerListCreateAPIView


urlpatterns = [
    path(f'{CustomerListCreateAPIView}/customer', CustomerListCreateAPIView.as_view(), name='customer-list-create-api-view')
]
