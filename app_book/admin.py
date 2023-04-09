from django.contrib import admin
from app_book.models import Book

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    pass