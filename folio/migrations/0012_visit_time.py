# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0011_auto_20180909_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
