from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^$', ClienteListView.as_view(), name="ClienteListView" ),
    url(r'^crear/$', ClienteCreateView.as_view(), name="ClienteCreateView" ),
    url(r'^editar/(?P<pk>[\w-]+)/$', ClienteUpdateiew.as_view(), name="ClienteUpdateiew" ),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', ClienteDeleteView.as_view(), name="ClienteDeleteView" ),
    url(r'^verificar/$', VerificarCliente, name="VerificarCliente" ),

]