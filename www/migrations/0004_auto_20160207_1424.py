# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_remove_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.CharField(max_length=250, null=True),
        ),
    ]