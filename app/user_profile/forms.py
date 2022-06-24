# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from salas.models import *

class UsuarioForm(forms.ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="", required=False,) 
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Nick/Username'}),label="Nick", required=False,) 
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Escribe el Email'}),label="Email", required=False,) 
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Escribe el Nombre'}),label="Nombre", required=False,) 
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Escribe el Apellido'}),label="Apellido", required=False,) 
	telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input','placeholder':'Escribe el Telefono'}),label="Teléfono", required=False,) 
	sala = forms.ModelChoiceField(queryset=Sala.objects.all(),widget=forms.Select(attrs={'class':'form-control round-input'}),label="Sala", required=False,)
	thumb = forms.FileField(required=False,)
	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','telefono','sala','thumb')

class ChangeNameForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input'}),label="Nombre", required=True,error_messages={'required': 'Debe ingresar el Nombre.'}) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control round-input'}),label="Apellido", required=True,error_messages={'required': 'Debe ingresar el Apellido.'})
    class Meta:
        model = User
        fields = ('first_name', 'last_name' )

class ChangeEmailForm(ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control round-input'}),required=True,error_messages={'required': 'Debe ingresar un Email.','valid':'valido'})
    class Meta:
        model = User
        fields = ('email',)