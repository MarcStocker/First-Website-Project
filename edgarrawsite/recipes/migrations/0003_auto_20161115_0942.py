# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20161115_0910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recipes',
            new_name='Recipe',
        ),
    ]
