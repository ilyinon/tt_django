# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Server',
        ),
        migrations.RemoveField(
            model_name='uptime',
            name='server',
        ),
        migrations.DeleteModel(
            name='Uptime',
        ),
    ]
