# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_addcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='addCode',
            field=models.CharField(default=uuid.uuid4, max_length=8, unique=True),
        ),
    ]
