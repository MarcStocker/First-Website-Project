# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20161115_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
