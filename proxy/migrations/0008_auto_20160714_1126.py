# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0007_auto_20160713_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy_config',
            name='ssl_cert',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='proxy_config',
            name='ssl_key',
            field=models.TextField(null=True),
        ),
    ]
