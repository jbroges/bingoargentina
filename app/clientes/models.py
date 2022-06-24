from __future__ import unicode_literals

from django.db import models
from salas.models import * 
from partidas.models import *
from django.utils import timezone

class Cliente(models.Model):
    sala = models.ForeignKey(Sala)
    nombre = models.CharField(max_length=150, blank=True)  
    apellido = models.CharField(max_length=150, blank=True)  
    dni = models.CharField(max_length=20, blank=True)  
    telefono = models.CharField(max_length=50, blank=True)  
    direccion = models.CharField(max_length=255, blank=True)  
    thumb = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    created_at = models.DateTimeField(editable=False,blank=False, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Cliente, self).save(*args, **kwargs)    
