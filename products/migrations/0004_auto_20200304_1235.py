# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-04 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_date_up'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='precio',
            new_name='price',
        ),
    ]
