from django.db import models
from django.utils.translation import gettext_lazy as _

class PaymentMethod(models.Model):
    class METHOD(models.TextChoices):
        MERCADO_PAGO = 'MP', _('Mercado Pago')
        CASH = 'CH' , _('Efectivo')
        DEBIT_CARD = 'DB', _('Tarjeta de debito')
        CREDIT_CARD =  'CC', _('Tarjeta de credito')
        TRASFER = 'TF' , _('Transferencia bancaria')
    
    payment_method = models.CharField(
        max_length = 2,
        choices = METHOD.choices,
        default = METHOD.CASH 
    )

    class Meta:
        abstract = True
    
class Editorial(models.Model):
    class EDITORIAL(models.TextChoices):
        ALICION = 1, _("Alición Editora")
        AMPERSAND = 2, _("Ampersand Editorial")
        ASUNTO = 3, _("Asunto Impreso Ediciones")
        ATLANTIDA= 4, _("Atlántida Editorial")
        AYARMANOT = 5, _("Ayarmanot Ediciones")
        CORREGIDOR= 6, _("Corregidor Ediciones")
        DE_MENTE = 7, _("De Mente Ediciones")
        DUNKEN = 8, _("Dunken Editorial")
        INTA = 9, _("Ediciones Inta")
        EDUCATIVAS = 10, _("Ediciones Novedades Educativas")
        QUILMES = 11, _("Editorial de la Universidad Nacional de Quilmes")
        HILO = 12, _("Editorial el Hilo de Ariadna")
        LOSADA = 13, _("Editorial Losada")
        MANSALVA = 14, _("Editorial Mansalva")
        BUENOS_AIRES = 15, _("Editorial Universidad de Buenos Aires")
        ELOISA = 16, _("Eloísa Cartonera")
        EMECE = 17, _("Emecé Editores")
        ZORZAL = 18, _("Libros del Zorzal")
        PERFIL = 19, _("Perfil Editorial")
        OTRO = 20 , _("Otra Editorial")

    publisher_company = models.IntegerField(
        choices = EDITORIAL.choices,
        default =  EDITORIAL.OTRO
    )