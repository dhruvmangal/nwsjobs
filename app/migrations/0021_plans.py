# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-03 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('plan_price', models.CharField(max_length=100)),
                ('plan_total_jobs', models.CharField(max_length=100)),
                ('plan_db_access', models.CharField(max_length=100)),
                ('plan_resume', models.CharField(max_length=100)),
                ('plan_validity_starts', models.DateTimeField(verbose_name='validity starts')),
                ('plan_validity_ends', models.DateTimeField(verbose_name='validity_ends')),
            ],
        ),
    ]
