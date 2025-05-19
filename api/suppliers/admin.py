from django.contrib import admin

from suppliers.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Supplier, SupplierAdmin)
