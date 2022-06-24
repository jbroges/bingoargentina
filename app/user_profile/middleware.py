from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions import get_cache 
class LIMITARUSER(MiddlewareMixin):

	def process_request(self, request):
		"""
		checkes si existe sesion igual en 2 maquinas y las cierra
		"""
		if request.user.is_authenticated():
			cache =  get_cache('default')
			cache_timeout = 86400
			cache_key = "user_pk_%s_restrict" % request.user.pk
			cache_value = cache.get(cache_key)
			if cache_value is not None:
				if request.session.session_key != cache_value:
					engine = import_module(settings.SESSION_ENGINE)
					session = engine.SessionStore(session_key=cache_value)
					session.delete()
					cache.set(cache_key, request.session.session_key,cache_timeout)
				else:
					cache.set(cache_key, request.session.session_key, cache_timeout)

		return None