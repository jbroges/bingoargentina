# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-09 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0003_auto_20171229_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='lineasEnJuego',
            field=models.IntegerField(default=3),
        ),
    ]
