# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import  PasswordChangeForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.views.generic import TemplateView
from django.utils.datastructures import MultiValueDictKeyError
from home.task import EnviarEmailDef
from .models import *
#CONTAR REGISTROS
#from django.db.models import Count
#co =  User.objects.annotate(cont = Count('pk'))
#print co[0].cont

from django.http import JsonResponse

class ChatEnLinea(TemplateView):
    template_name='chat-en-linea.html'
    def chat(self):
    	res = Chat.objects.all().order_by('-pk')[:30]
    	obj = []
    	return sorted(res, key=lambda object: object.id)

def EscribirChat(request):

	chat  = Chat.objects.create(userE = request.user, mensaje = request.GET['msj'],userR='todos')
	fire = {}
	fire['emisor'] = request.user.username
	fire['receptor'] = 'todos'
	fire['mensaje'] = request.GET['msj']
	fire['time'] = chat.created_at
	fire['thumb'] = str(request.user.userprofile.thumb)
	fire['sala'] = str(request.user.userprofile.sala.nombre)
	return JsonResponse(fire)