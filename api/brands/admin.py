from django.contrib import admin

from brands.models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Brand, BrandAdmin)
