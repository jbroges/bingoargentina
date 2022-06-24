# -*- encoding: utf-8 -*-

from requests import request, HTTPError

from django.core.files.base import ContentFile
from .models import UserProfile
from pprint import pprint
from semilla.views import AsignarDef
from configuracion.views import EnviarEmailDef

def update_avatar(backend, user, response, details,is_new=False,*args,**kwargs):
	if is_new:
		profile = UserProfile.objects.create(user_id=user.id)
		profile.save()
		AsignarDef(user.id)

 
		if backend.name == 'facebook':
			url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
			parametro={'type': 'large'}
		
		elif backend.name == 'twitter':
			url = response.get('profile_image_url').replace('_normal','')
			parametro = {}
		try:
			response = request('GET', url, params=parametro)
			response.raise_for_status()
		except HTTPError:
			pass
		else:
			profile = UserProfile.objects.get(user_id=user.id)
	        profile.thumb.save('{0}_social.jpg'.format(user.username), ContentFile(response.content))
	        profile.save()
	        titulo = 'Almorir.me verficacion de email'
	        msj = 'Saludos Gracias por utilizar los servicios de mensajeria post mortem de Almorir.me, en este momento su emnil no esta verificado de click en esiguente vinculo para verficar su email: Verificar email en Almorir.me  El equipo de radiowebdigital.com Gracias'
	        html = '<table style="width:600px;margin:auto"> <tr><td align="center" style="text-align:center;"><img src="http://almorir.me/static/img/logo250.png" alt="">      </td>   </tr>   <tr>        <td style="background:#ccc">            <p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de mensajería post mortem de <a href="http://almorir.me"> Almorir.me</a>, en este momento su <b>email no esta verificado</b> visite el siguiente enlace para verificar su email: <br> <br><a href="http://almorir.me/verificar-email/' + str(user.id) + '/">Verificar email en Almorir.me</a> <br><br>  El equipo de <b>Almorir.me</b> Gracias         </p>        </td>   </tr></table>'
	        EnviarEmailDef.apply_async((titulo,msj, html, user.email),countdown=10)
