from django.db import models
from app_core.models import PaymentMethod
from django.utils.translation import gettext_lazy as _


class Warehouse(PaymentMethod):
    warehouse_id = models.IntegerField(primary_key=True )
    address =  models.CharField(max_length=200 , blank=False , null=False )
    delivery = models.BooleanField(default=False)
    

class WarehouseList(models.Model):
    warehouse_id = models.ForeignKey(
        "app_warehouse.WareHouse",
        related_name = "app_warehouse",
        on_delete=models.DO_NOTHING
    )
    book_id = models.ForeignKey(
        "app_book.Book",
        related_name="app_book",
        on_delete=models.CASCADE
    )
    available = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )
    amount = models.IntegerField(
        null=False,
        default = 10,
        blank=False,
    )