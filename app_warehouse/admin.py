from django.contrib import admin
from app_warehouse.models import Warehouse,WarehouseList

@admin.register(Warehouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Warehouse._meta.get_fields()]

@admin.register(WarehouseList)
class WarehouseListAdmin(admin.ModelAdmin):
    pass