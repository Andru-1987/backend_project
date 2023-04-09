from django.contrib import admin
from app_books.models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['__all__']