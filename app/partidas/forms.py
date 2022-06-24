# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *

DATE_INPUT_FORMATS = ['%d-%m-%Y']


class PartidaForm(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="",required=False) 	
	fecha = forms.DateField(label="Fecha",widget=forms.DateInput(format='%Y-%m-%d',attrs={'type':'text','class': 'form-control round-input','placeholder':'Ingrese la Fecha'}),input_formats=DATE_INPUT_FORMATS,required=False,) 
	organiza = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Razon Social'}),label="Organiza",required=False) 	
	sorteo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Dia y Hora del Sorteo'}),label="Sorteo",required=False) 	
	transmite = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Emisora que Transmite'}),label="Transmite",required=False) 	
	precio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Precio'}),label="Precio",required=False) 	
	premio_1 = forms.BooleanField(label="1er Premio",required=False)
	premio_2 = forms.BooleanField(label="2do Premio",required=False)
	premio_3 = forms.BooleanField(label="3er Premio",required=False)
	premio_4 = forms.BooleanField(label="4to Premio",required=False)
	premio_5 = forms.BooleanField(label="5to Premio",required=False)
	premio_6 = forms.BooleanField(label="6to Premio",required=False)
	premio_7 = forms.BooleanField(label="7mo Premio",required=False)
	monto_1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	monto_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	monto_3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	monto_4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	monto_5 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	monto_6 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	monto_7 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Monto'}),required=False)
	t1f = forms.CharField(widget=forms.TextInput(attrs={'value':'#FFFFFF','type': 'color',}),label='Tabla 1',required=False)
	t1l = forms.CharField(widget=forms.TextInput(attrs={'type': 'color',}),required=False)
	t2f = forms.CharField(widget=forms.TextInput(attrs={'value':'#FFFFFF','type': 'color',}),label='Tabla 2',required=False)
	t2l = forms.CharField(widget=forms.TextInput(attrs={'type': 'color',}),required=False)
	t3f = forms.CharField(widget=forms.TextInput(attrs={'value':'#FFFFFF','type': 'color',}),label='Tabla 3',required=False)
	t3l = forms.CharField(widget=forms.TextInput(attrs={'type': 'color',}),required=False)
	lineasEnJuego = forms.ChoiceField(choices=(('3','3'),('2','2'),('1','1'),), widget=forms.Select(attrs={'class':'form-control round-input'}),label="Lineas en  Juego", required=False,)
	cartonBlank = forms.ChoiceField(choices=(('NO','NO'),('SI','SI'),), widget=forms.Select(attrs={'class':'form-control round-input'}),label="Carton Sin Diseño", required=False,)
	thumb = forms.FileField(required=False,)
	condiciones = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Reglas + Condiiones de Juego'}),label="Condiciones",required=False,)
	class Meta:
		model = Partida
		fields = ('fecha','organiza','sorteo','precio','premio_1','premio_2','premio_3','premio_4','premio_5','premio_6','premio_7','monto_1','monto_2','monto_3','monto_4','monto_5','monto_6','monto_7','thumb','id','transmite','condiciones','lineasEnJuego','t1f','t1l','t2f','t2l','t3f','t3l','cartonBlank')