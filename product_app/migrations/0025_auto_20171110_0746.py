# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0024_auto_20171109_1953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Biography',
            new_name='UserProfile',
        ),
    ]