# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-18 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0005_project_imagephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='folio.Skill'),
        ),
    ]