# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0037_auto_20170327_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumarea',
            name='children',
        ),
        migrations.AddField(
            model_name='curriculumarea',
            name='children',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_curriculum_area', to='topics.CurriculumArea'),
        ),
    ]
