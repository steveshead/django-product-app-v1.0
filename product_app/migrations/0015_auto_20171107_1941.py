# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 03:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0014_auto_20171106_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biography',
            name='user',
        ),
        migrations.DeleteModel(
            name='Biography',
        ),
    ]
