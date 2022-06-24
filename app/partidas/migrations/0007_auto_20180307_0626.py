# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-07 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0006_partida_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='ganador_6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partida',
            name='ganador_7',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_6',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='partida',
            name='monto_7',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='partida',
            name='premio_6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partida',
            name='premio_7',
            field=models.BooleanField(default=False),
        ),
    ]