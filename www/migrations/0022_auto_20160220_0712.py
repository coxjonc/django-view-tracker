# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0021_byline_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='byline',
            name='slug',
        ),
    ]
