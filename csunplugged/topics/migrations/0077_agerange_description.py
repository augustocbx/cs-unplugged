# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0076_remove_lesson_sorting_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='agerange',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]