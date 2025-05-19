from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Product, ProductAdmin)
