# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0105_auto_20171027_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='other_resources',
            field=models.TextField(default='', null=True),
        ),
    ]
