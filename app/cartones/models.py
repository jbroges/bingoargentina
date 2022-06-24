from __future__ import unicode_literals

from django.db import models
# Create your models here.
from clientes.models import Cliente

class Carton(models.Model):
    l1_1 = models.CharField(max_length=2, blank=True)  
    l1_2 = models.CharField(max_length=2, blank=True)  
    l1_3 = models.CharField(max_length=2, blank=True)  
    l1_4 = models.CharField(max_length=2, blank=True)  
    l1_5 = models.CharField(max_length=2, blank=True)  
    l1_6 = models.CharField(max_length=2, blank=True)  
    l1_7 = models.CharField(max_length=2, blank=True)  
    l1_8 = models.CharField(max_length=2, blank=True)  
    l1_9 = models.CharField(max_length=2, blank=True)  
    l2_1 = models.CharField(max_length=2, blank=True)  
    l2_2 = models.CharField(max_length=2, blank=True)  
    l2_3 = models.CharField(max_length=2, blank=True)  
    l2_4 = models.CharField(max_length=2, blank=True)  
    l2_5 = models.CharField(max_length=2, blank=True)  
    l2_6 = models.CharField(max_length=2, blank=True)  
    l2_7 = models.CharField(max_length=2, blank=True)  
    l2_8 = models.CharField(max_length=2, blank=True)  
    l2_9 = models.CharField(max_length=2, blank=True)  
    l3_1 = models.CharField(max_length=2, blank=True)  
    l3_2 = models.CharField(max_length=2, blank=True)  
    l3_3 = models.CharField(max_length=2, blank=True)  
    l3_4 = models.CharField(max_length=2, blank=True)  
    l3_5 = models.CharField(max_length=2, blank=True)  
    l3_6 = models.CharField(max_length=2, blank=True)  
    l3_7 = models.CharField(max_length=2, blank=True)  
    l3_8 = models.CharField(max_length=2, blank=True)  
    l3_9 = models.CharField(max_length=2, blank=True)  
  

#asignaciones
from salas.models import * 
from partidas.models import *
from django.utils import timezone
class Asignacion(models.Model):
    sala = models.ForeignKey(Sala)
    partida = models.ForeignKey(Partida)
    correlat_ini = models.IntegerField() 
    correlat_fin = models.IntegerField() 
    created_at = models.DateTimeField(editable=False,blank=False, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Asignacion, self).save(*args, **kwargs)    
    class Meta:
        ordering = ["-id"]
  

class Impresion(models.Model):
    partida = models.ForeignKey(Partida)
    ganador_1 = models.BooleanField(default=False)
    linea_1 = models.IntegerField(default = 0)
    ganador_2 = models.BooleanField(default=False)
    linea_2 = models.IntegerField(default = 0)
    ganador_3 = models.BooleanField(default=False)
    linea_3 = models.IntegerField(default = 0)
    ganador_4 = models.BooleanField(default=False)
    linea_4 = models.IntegerField(default = 0)
    ganador_5 = models.BooleanField(default=False)
    linea_5 = models.IntegerField(default = 0)
    ganador_6 = models.BooleanField(default=False)
    linea_6 = models.IntegerField(default = 0)
    ganador_7 = models.BooleanField(default=False)
    linea_7 = models.IntegerField(default = 0)
    ganador = models.BooleanField(default=False)
    ganador_at = models.DateTimeField(blank=False, null=True)
    carton = models.ForeignKey(Carton)
    numeroCarton = models.IntegerField(default = 0)
    participa = models.CharField(max_length=2, default = 'E')  
    created_at = models.DateTimeField(editable=False,blank=False, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Impresion, self).save(*args, **kwargs)    
    class Meta:
        ordering = ["-id"]
   