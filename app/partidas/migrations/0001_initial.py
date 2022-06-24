# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-27 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balota', models.CharField(blank=True, max_length=2)),
                ('orden', models.CharField(blank=True, max_length=2)),
                ('created_at', models.DateTimeField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiza', models.CharField(blank=True, max_length=200)),
                ('sorteo', models.CharField(blank=True, max_length=200)),
                ('precio', models.CharField(blank=True, max_length=200)),
                ('transmite', models.CharField(blank=True, max_length=200)),
                ('premio_1', models.BooleanField(default=False)),
                ('monto_1', models.CharField(default='0', max_length=50)),
                ('ganador_1', models.BooleanField(default=False)),
                ('premio_2', models.BooleanField(default=False)),
                ('monto_2', models.CharField(default='0', max_length=50)),
                ('ganador_2', models.BooleanField(default=False)),
                ('premio_3', models.BooleanField(default=False)),
                ('monto_3', models.CharField(default='0', max_length=50)),
                ('ganador_3', models.BooleanField(default=False)),
                ('premio_4', models.BooleanField(default=False)),
                ('monto_4', models.CharField(default='0', max_length=50)),
                ('ganador_4', models.BooleanField(default=False)),
                ('premio_5', models.BooleanField(default=False)),
                ('monto_5', models.CharField(default='0', max_length=50)),
                ('ganador_5', models.BooleanField(default=False)),
                ('termino', models.BooleanField(default=False)),
                ('inicio', models.BooleanField(default=False)),
                ('thumb', models.ImageField(default='pic_folder/no-image-thumb.png', upload_to='salas/logos/')),
                ('created_at', models.DateTimeField(editable=False, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='jugada',
            name='partida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partidas.Partida'),
        ),
    ]
