# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['in_progress']},
        ),
    ]
