# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-10 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wwwapp', '0050_auto_20190704_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='max_points',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
