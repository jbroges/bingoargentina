# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170520_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
