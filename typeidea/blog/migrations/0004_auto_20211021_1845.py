# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-21 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211021_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pv',
        ),
        migrations.RemoveField(
            model_name='category',
            name='uv',
        ),
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
