# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0103_auto_20171027_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='other_resources',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='other_resources_de',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='other_resources_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='other_resources_fr',
            field=models.TextField(null=True),
        ),
    ]
