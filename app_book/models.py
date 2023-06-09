import re
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# a modo de testing y experimentacion
# voy a usar el FileSystem Built in function de Django


from django.core.files.storage.filesystem import FileSystemStorage

FS = FileSystemStorage(location = "/media/pictures")


def validate_ISBN(isbn):
    regex = r'978(?:-?\d){10}' 
    if re.search(regex , isbn , re.IGNORECASE) :
       return isbn
    else:
        raise ValidationError('Not Valid ISBN')


class Book(models.Model):

    FIRST = '1ST'
    SECOND = '2ND'
    THIRD =  '3RD'
    OTHER = 'OTH'

    VERSION_CHOICES = [
        (FIRST, 'First'),
        (SECOND, 'Second'),
        (THIRD, 'Thid'),
        (OTHER, 'Other')
    ]


    INGLES = 'EN'
    SPANISH = 'ES'
    ALEMAN = 'DE'
    OTRO = 'OT'

    LANG_CHOICES = [
        (INGLES , 'Ingles'),
        (SPANISH, 'Espanol'),
        (ALEMAN, 'Aleman'),
        (OTRO, 'Otro'),
    ]

    class MONEY(models.TextChoices):
        DOLARES = 'US' , _('Dolares')
        PESOS = 'PS' , _('Pesos Argentinos')
        EUROS = 'EU' ,_('Euros')


    book_id = models.IntegerField(primary_key=True )
    name    = models.CharField(max_length=200 , blank=False , null=False )
    pic     = models.ImageField(
        storage=FS,
        default=None,
        blank=True,
        null=True
    )
    ISBN    = models.CharField( 
        max_length=13,
        validators=[validate_ISBN],
        default="978-3-16-148410-0"
    
    )
    author_id = models.ManyToManyField(
        "app_author.Author",
        related_name="app_author" ,
        # on_delete = models.DO_NOTHING,    
    )
    pages = models.IntegerField(default=100, null=False , blank=True) 
    
    languages = models.CharField(
        max_length = 2,
        choices = LANG_CHOICES,
        default = SPANISH,
    ) 
    
    release_date = models.DateField(_("Date"), auto_now_add=True)
    
    publishing_version = models.CharField(
        max_length = 3 ,
        choices = VERSION_CHOICES,
        default = FIRST
    )
    price = models.IntegerField(blank = False , null = True , default = None)
    currency = models.CharField(
        max_length = 2,
        choices = MONEY.choices,
        default = MONEY.PESOS
    )

    '''
    si bien no es lo mejor el utilizar dos conceptos distintos en el mismo proyecto
    el proposito de utilizar este patron distinto es para conocer la logica que tiene el 
    usar otras herramientas de choices, en enregas futuras voy a utilizar solamente la
    opcion por clases.
    Es mucho mas practica
    '''


    def _str_(self):
        return super().__str__()


