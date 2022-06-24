from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from user_profile.models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import time
from partidas.models import * 
from cartones.models import * 

# Create your views here.
class LoginInt(TemplateView):
	template_name="loginInt.html"
	def get(self, request, *args, **kwargs):
		if	self.request.user.id is None:
			return super(LoginInt, self).get(request, *args, **kwargs)
		else: 
			return redirect('/app/')

class Recuperar(TemplateView):
	template_name="recuperar.html"

# Create your views here.
class Index(TemplateView):
	template_name = "base.html"
	@method_decorator(login_required(login_url='/'))
	def dispatch(self, *args, **kwargs):
		#send_mail('Subject here', 'Here is the message.', 'Bingos Marvel <noreply@bingosmarvel.com>', ['jbroges@gmail.com'], fail_silently=False)
		return super(Index, self).dispatch(*args, **kwargs)
	def partida(self):
		partida= Partida.objects.filter(termino=False)[:1] 
		if partida:
			id = partida[0].id
		else:
			id='0'
		return id
	def vendidos(self):
		partida= Partida.objects.filter(termino=False)[:1] 
		if not partida:
			return 0
		#CARTONES VENDIDOS GENERAL
		cartonvendidos = Impresion.objects.filter(partida_id=partida[0].id, participa = 'S').count()    
		return cartonvendidos
	def ensala(self):
		partida= Partida.objects.filter(termino=False)[:1] 
		if not partida:
			return 0
		#cartones en sala	
		cartonensala = Impresion.objects.filter(partida_id=partida[0].id).count()    
		return cartonensala
	def premiados(self):
		partida= Partida.objects.filter(termino=False)[:1] 
		if not partida:
			return 0
		if self.request.user.is_superuser:
			g1 =  Impresion.objects.filter(partida_id=partida[0].id,ganador_1=1).count()
			g2 =  Impresion.objects.filter(partida_id=partida[0].id,ganador_2=1).count()		
			g3 =  Impresion.objects.filter(partida_id=partida[0].id,ganador_3=1).count()		
			g4 =  Impresion.objects.filter(partida_id=partida[0].id,ganador_4=1).count()		
			g5 =  Impresion.objects.filter(partida_id=partida[0].id,ganador_5=1).count()		
			return g1 + g2 + g3 + g4 + g5
		g1 =  Impresion.objects.filter(partida_id=partida[0].id,propietario__sala_id = self.request.user.userprofile.sala.id,ganador_1=1).count()
		g2 =  Impresion.objects.filter(partida_id=partida[0].id,propietario__sala_id = self.request.user.userprofile.sala.id,ganador_2=1).count()		
		g3 =  Impresion.objects.filter(partida_id=partida[0].id,propietario__sala_id = self.request.user.userprofile.sala.id,ganador_3=1).count()		
		g4 =  Impresion.objects.filter(partida_id=partida[0].id,propietario__sala_id = self.request.user.userprofile.sala.id,ganador_4=1).count()		
		g5 =  Impresion.objects.filter(partida_id=partida[0].id,propietario__sala_id = self.request.user.userprofile.sala.id,ganador_5=1).count()		
		return g1 + g2 + g3 + g4 + g5