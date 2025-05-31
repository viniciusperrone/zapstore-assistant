from django.urls import path

from utils.api import BASIC_API_URL


urlpatterns = [
    path(f'{BASIC_API_URL}/orders')
]
