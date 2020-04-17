# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-14 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxfWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]
