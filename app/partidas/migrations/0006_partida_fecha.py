# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-10 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0005_jugada_premio'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='fecha',
            field=models.DateField(default='1990-01-01'),
        ),
    ]