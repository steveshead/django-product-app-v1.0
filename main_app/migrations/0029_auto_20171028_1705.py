# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_auto_20171028_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='product_images'),
        ),
    ]
