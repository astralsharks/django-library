# Generated by Django 2.2.12 on 2020-05-31 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]
