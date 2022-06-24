# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *

class ConfigForm(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="",required=False) 	
	tiempoMaster = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Tiempo Primario en MILISEGUNDOS'}),label="Tiempo Primario",required=False) 	
	tiempoInter = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':"Tiempo Segundario en MILISEGUNDOS"}),label="Tiempo Segundario",required=False) 	
	class Meta:
		model = Configuracion
		fields = ('id','tipopartida','theme','tiempoMaster','tiempoInter')