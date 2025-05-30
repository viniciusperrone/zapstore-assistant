from django.contrib import admin
from django.urls import path, include

from utils.api import BASIC_API_URL
from core.views import get_all_data


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('products.urls')),
    path('', include('suppliers.urls')),
    path('', include('inventory.urls')),
    path('', include('sales.urls')),
    path('', include('customers.urls')),

    path(f'{BASIC_API_URL}/all_data', get_all_data, name='get-all-data')
]
