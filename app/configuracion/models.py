from __future__ import unicode_literals

from django.db import models
# Create your models here.
TipoPartida = [('MANUAL','MANUAL'),('AUTOMATICO','AUTOMATICO')]
TipoTheme = [('DARK','DARK'),('LIGHT','LIGHT')]


class Configuracion(models.Model):
	partida = models.FileField(upload_to='cargas/excel/',null=True)
	asignaciones = models.FileField(upload_to='cargas/excel/', null=True)
	tipopartida = models.CharField(max_length=12, choices=TipoPartida,default='MANUAL')
	tiempoMaster = models.CharField(max_length=5, blank=True)
	tiempoInter = models.CharField(max_length=5, blank=True)
	theme = models.CharField(max_length=12, choices=TipoTheme,default='DARK')