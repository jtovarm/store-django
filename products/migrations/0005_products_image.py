# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-03-05 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200304_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='upload-product/'),
            preserve_default=False,
        ),
    ]
