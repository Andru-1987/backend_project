# Generated by Django 4.2 on 2023-04-11 20:57

import app_book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_book', '0002_book_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default='978-3-16-148410-0', max_length=13, validators=[app_book.models.validate_ISBN]),
        ),
    ]
