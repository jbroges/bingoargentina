# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *
from salas.models import *


class ClienteForm(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="",required=False) 	
	nombre = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Nombre'}),label="Nombre",required=False,)
	apellido = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Apellido'}),label="Apellido",required=False,)
	dni = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Cédula de Identidad'}),label="Cédula",required=False,)
	telefono = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Teléfono'}),label="Teléfono",required=False,)
	direccion = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Dirección'}),label="Dirección",required=False,)
	sala = forms.ModelChoiceField(queryset=Sala.objects.filter(activa='Si'),widget=forms.Select(attrs={'class':'form-control round-input'}),label="Sala", required=False,)
	thumb = forms.FileField(required=False,)
	class Meta:
		model = Cliente
		fields = ('nombre','apellido','dni','telefono','direccion','thumb','sala','id')

