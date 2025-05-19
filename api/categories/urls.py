from django.urls import path

from utils.api import BASIC_API_URL
from categories.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView


urlpatterns = [
    path(f'{BASIC_API_URL}/category', CategoryListCreateAPIView.as_view(), name='category-create-list-api-view'),
    path(f'{BASIC_API_URL}/category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail-api-view'),
]
