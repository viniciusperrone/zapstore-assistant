from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    ...


admin.site.register(Order, OrderAdmin)
