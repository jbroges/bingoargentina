# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *
from salas.models import *
from partidas.models import *
import time

DATE_INPUT_FORMATS = ['%m-%d-%Y']


class AsignacionForm(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="",required=False) 	
	partida = forms.ModelChoiceField(queryset=Partida.objects.filter(inicio=False), widget=forms.Select(attrs={'class':'form-control round-input'}),label="Partida", required=False,)
	correlat_ini = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Correlativo Inicial'}),label="Corr. Inicio",required=False,)
	numcarton = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Numero de Carton'}),label="Carton Nº",required=False,)
	correlat_fin = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Correlativo Final'}),label="Corr. Fin",required=False,)
	sala = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden','value':'1'}),label="", required=False,)
	class Meta:
		model = Asignacion
		fields = ('partida','correlat_ini','correlat_fin','sala','id')

 
class ImprimirForm(ModelForm):
	cantidad = forms.CharField( widget=forms.TextInput(attrs={'value':'1','type':'number','class': 'form-control round-input','placeholder':'Cantidad a Imprimir'}),label="Nº de Cartones",required=False,)
	class Meta:
		model = Impresion
		fields = ('id',)
