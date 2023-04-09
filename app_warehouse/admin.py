from django.contrib import admin
from app_warehouse.models import Warehouse

@admin.register(Warehouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display = ['__all__']