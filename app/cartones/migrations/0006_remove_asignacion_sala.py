# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-16 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartones', '0005_impresion_participa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignacion',
            name='sala',
        ),
    ]
