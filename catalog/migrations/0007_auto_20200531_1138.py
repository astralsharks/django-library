# Generated by Django 2.2.12 on 2020-05-31 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200531_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adaptation',
            name='year',
            field=models.PositiveIntegerField(help_text='Enter a publishing year', null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1800)], verbose_name='Release year'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveIntegerField(help_text='Enter a publishing year', null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1800)], verbose_name='Publishing year'),
        ),
    ]
