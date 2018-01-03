# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-26 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=128)),
                ('service_time', models.DateField()),
                ('contact', models.CharField(max_length=30)),
                ('stack', models.CharField(max_length=128, null=True)),
                ('bandwith', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]