import re
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.translation import gettext_lazy as _


def validate_ISBN(isbn):
    regex = r'978(?:-?\d){10}' 
    if re.search(regex , isbn , re.IGNORECASE) :
       return isbn
    else:
        raise ValidationError('Not Valid ISBN')


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True )
    name = models.CharField(max_length=200 , blank=False , null=False )
    ISBN = models.CharField(max_length=10,validators=[validate_ISBN])
    author_id = models.ManyToManyField("app_authors.Authors", related_name="app_authors" , on_delete = models.DO_NOTHING)
    pages = models.IntegerField(default=100, null=False , blank=True) 
    languages = models.TextChoices() 
    release_date = models.DateField(_("Date"), auto_now_add=True)
    publishing_version = 
    price = models. 
    currency = 


