# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-20 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20160617_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
