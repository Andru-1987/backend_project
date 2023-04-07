from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):

    class PaymentMethod(models.TextChoices):
        MERCADO_PAGO = 'MP', _('Mercado Pago')
        CASH = 'CH' , _('Efectivo')
        DEBIT_CARD = 'DB', _('Tarjeta de debito')
        CREDIT_CARD =  'CC', _('Tarjeta de credito')
        TRASFER = 'TF' , _('Transferencia bancaria')

    warehouse_id = models.IntegerField(primary_key=True,unique=True)
    address = models.CharField(max_length=200,null=False)
    delivery = models.BooleanField(default=True , blank=False, null=False)
    payment_method = models.CharField(
        max_length = 2,
        choices = PaymentMethod.choices,
        default = PaymentMethod.CASH 
    )

    def __str__(self) -> str:
        return super().__str__()