# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 04:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0016_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Biography',
        ),
        migrations.RenameField(
            model_name='biography',
            old_name='department',
            new_name='biography',
        ),
    ]
