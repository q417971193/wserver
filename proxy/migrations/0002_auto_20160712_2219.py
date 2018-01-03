# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [

        migrations.AddField(
            model_name='proxy_config',
            name='balancer_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='upstream_config',
            name='fail_timeout',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upstream_config',
            name='max_fails',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
