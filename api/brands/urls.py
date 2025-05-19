from django.urls import path

from utils.api import BASIC_API_URL
from brands.views import BrandListCreateAPIView

urlpatterns = [
    path(f'{BASIC_API_URL}/brand', BrandListCreateAPIView.as_view(), name='brand-create-list-view')
]
