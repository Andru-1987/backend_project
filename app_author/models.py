from django.db import models
from django.utils.translation import gettext_lazy as _
from app_core.models import Editorial

class Author(Editorial):
    
    author_id = models.IntegerField(primary_key=True )
    names = models.CharField(max_length=100 , blank = False , null = False)
    last_names = models.CharField(max_length=100 , blank = False , null = False)

    def __str__(self) -> str:
        return super().__str__()