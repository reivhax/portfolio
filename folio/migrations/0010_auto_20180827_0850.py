# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0009_auto_20180827_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='folio.Skill'),
        ),
    ]
