# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0018_auto_20171107_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='userName',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]