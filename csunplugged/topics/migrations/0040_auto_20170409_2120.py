# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0039_auto_20170327_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='other_resources',
            field=models.TextField(null=True),
        ),
    ]
