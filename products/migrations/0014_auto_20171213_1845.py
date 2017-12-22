# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 02:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20171209_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_file',
            field=models.FileField(blank=True, null=True, upload_to='product_files', validators=[django.core.validators.FileExtensionValidator(['zip'])]),
        ),
    ]