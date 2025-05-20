from django.contrib import admin

from sales.models import Sales


class SalesAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')


admin.site.register(Sales, SalesAdmin)
