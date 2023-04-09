from django.contrib import admin
from app_authors.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__all__']
