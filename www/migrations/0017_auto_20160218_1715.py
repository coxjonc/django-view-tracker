# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0016_auto_20160218_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='names',
            new_name='bylines',
        ),
    ]
