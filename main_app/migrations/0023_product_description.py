# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_auto_20171022_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='description', max_length=300),
        ),
    ]
