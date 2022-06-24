from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
# A new user has registered.




class Partida(models.Model):
    fecha = models.DateField(default='1990-01-01')    
    organiza = models.CharField(max_length=200, blank=True)  
    sorteo = models.CharField(max_length=200, blank=True)  
    precio = models.CharField(max_length=200, blank=True)  
    transmite = models.CharField(max_length=200, blank=True)  
    condiciones = models.CharField(max_length=250, blank=True)  
    premio_1 = models.BooleanField(default=False)
    monto_1 = models.CharField(max_length=50, default='0')
    ganador_1 = models.BooleanField(default=False)
    premio_2 = models.BooleanField(default=False)
    monto_2 = models.CharField(max_length=50, default='0')
    ganador_2 = models.BooleanField(default=False)
    premio_3 = models.BooleanField(default=False)
    monto_3 = models.CharField(max_length=50, default='0')
    ganador_3 = models.BooleanField(default=False)
    premio_4 = models.BooleanField(default=False)
    monto_4 = models.CharField(max_length=50, default='0')
    ganador_4 = models.BooleanField(default=False)
    premio_5 = models.BooleanField(default=False)
    monto_5 = models.CharField(max_length=50, default='0')
    ganador_5 = models.BooleanField(default=False)
    premio_6 = models.BooleanField(default=False)
    monto_6 = models.CharField(max_length=50, default='0')
    ganador_6 = models.BooleanField(default=False)
    premio_7 = models.BooleanField(default=False)
    monto_7 = models.CharField(max_length=50, default='0')
    ganador_7 = models.BooleanField(default=False)
    termino = models.BooleanField(default=False)
    inicio = models.BooleanField(default=False)
    thumb = models.ImageField(upload_to = 'salas/logos/', default = 'pic_folder/bingo.png')
    t1f = models.CharField(max_length=200, blank=True)  
    t1l = models.CharField(max_length=200, blank=True)  
    t2f = models.CharField(max_length=200, blank=True)  
    t2l = models.CharField(max_length=200, blank=True)  
    t3f = models.CharField(max_length=200, blank=True)  
    t3l = models.CharField(max_length=200, blank=True)  
    lineasEnJuego  = models.IntegerField(default = 3)
    cartonBlank = models.CharField(max_length=2, default='NO')    
    created_at = models.DateTimeField(editable=False,blank=False, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        return super(Partida, self).save(*args, **kwargs)    
    def __str__(self):
        return self.organiza

class Jugada(models.Model):
    partida = models.ForeignKey(Partida)
    balota = models.CharField(max_length=2, blank=True)
    orden = models.CharField(max_length=2, blank=True)
    premio = models.CharField(max_length=10, blank=True)   
    created_at = models.DateTimeField(editable=False,blank=False, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        return super(Jugada, self).save(*args, **kwargs)    
    