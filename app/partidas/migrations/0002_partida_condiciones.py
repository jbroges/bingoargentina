# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-28 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='condiciones',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
