# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-03 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190203_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='about',
        ),
        migrations.RemoveField(
            model_name='college',
            name='address',
        ),
        migrations.RemoveField(
            model_name='college',
            name='contact_person',
        ),
    ]
