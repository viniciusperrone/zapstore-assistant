from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('products.urls')),
    path('', include('suppliers.urls')),
    path('', include('inventory.urls')),
    path('', include('sales.urls'))
]
