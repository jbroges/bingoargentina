from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
# A new user has registered.

class Chat(models.Model):
	userE =  models.ForeignKey(User)
	userR =  models.CharField(max_length=50, blank=True)  
	mensaje = models.CharField(max_length=200, blank=True)  
	created_at = models.DateTimeField(editable=False,blank=False, null=True)
	def save(self, *args, **kwargs):
		if not self.id:
			self.created_at = datetime.datetime.now()
		return super(Chat, self).save(*args, **kwargs)    


