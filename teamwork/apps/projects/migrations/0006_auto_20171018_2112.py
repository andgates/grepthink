# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 04:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20171018_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsr',
            name='percent_contribution',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
