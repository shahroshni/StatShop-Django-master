# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-25 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.99, max_digits=19),
        ),
    ]