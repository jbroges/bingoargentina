from configuracion.models import *
from django.core.exceptions import ObjectDoesNotExist

def tiempo(request):
	try:
		c = Configuracion.objects.get(pk=1)
		return {'primario':c.tiempoMaster, 'intermedio':c.tiempoInter,'request':request}
	except ObjectDoesNotExist:
		pass
	return {'request':request}
