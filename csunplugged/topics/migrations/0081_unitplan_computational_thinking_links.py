# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0080_auto_20170618_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitplan',
            name='computational_thinking_links',
            field=models.TextField(null=True),
        ),
    ]
