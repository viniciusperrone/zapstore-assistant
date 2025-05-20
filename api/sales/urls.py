from django.urls import path

from sales.views import SalesListCreateAPIView
from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/sales', SalesListCreateAPIView.as_view(), name='sales-list-create-api-view')
]
