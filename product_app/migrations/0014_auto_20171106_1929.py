# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0013_auto_20171105_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='biography',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]