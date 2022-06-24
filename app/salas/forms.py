# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *



class SalaForm(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="",required=False) 	
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Nombre'}),label="Nombre",required=False,) 
	direccion = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Direecion'}),label="Dirección",required=False,)
	thumb = forms.FileField(required=False,)
	class Meta:
		model = Sala
		fields = ('nombre','direccion','thumb','id')

 