from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
# A new user has registered.


class Sala(models.Model):
    nombre = models.CharField(max_length=50, blank=True)  
    direccion = models.CharField(max_length=250, blank=True)  
    activa =  models.CharField(max_length=2, default = 'Si')  
    thumb = models.ImageField(upload_to = 'salas/logos/', default = 'pic_folder/no-image-thumb.png')
    created_at = models.DateTimeField(editable=False, blank=False, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        return super(Sala, self).save(*args, **kwargs)    
    def __str__(self):
    	return self.nombre
   