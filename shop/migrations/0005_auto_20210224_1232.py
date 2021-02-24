# Generated by Django 3.0.5 on 2021-02-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_book_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sold',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default='False'),
        ),
    ]
