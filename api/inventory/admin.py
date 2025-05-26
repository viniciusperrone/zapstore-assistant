from django.contrib import admin

from inventory.models import Inflow


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier')


admin.site.register(Inflow, InventoryAdmin)
