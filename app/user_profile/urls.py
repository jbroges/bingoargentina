from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^login/', LoginDef, name="login" ),
   	url(r'^crear/$', UsuarioCreateView.as_view(), name="UsuarioCreateView" ),
    url(r'^editar/(?P<pk>[\w-]+)/$', UsuarioUpdateView.as_view(), name="UsuarioUpdateView" ),
    url(r'^eliminar/(?P<pk>[\w-]+)/$', UsuarioDeleteView.as_view(), name="UsuarioDeleteView" ),
    url(r'^$', ListUsuariosView.as_view(), name="ListUsuariosView" ),
    url(r'^check-user/', CheckUserDef, name="check-user"),
    url(r'^check-email/', CheckEmailDef, name="check-email"),

]