# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-10 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartones', '0004_impresion_numerocarton'),
    ]

    operations = [
        migrations.AddField(
            model_name='impresion',
            name='participa',
            field=models.CharField(default='E', max_length=2),
        ),
    ]