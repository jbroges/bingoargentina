from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^$', SalasListView.as_view(), name="Sala" ),
    url(r'^crear/$', SalaCreateView.as_view(), name="SalaCreate" ),
    url(r'^editar/(?P<pk>[\w-]+)/$', SalaUpdateView.as_view(), name="SalaEdit" ),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', SalaDeleteView.as_view(), name="SalaDeleteView" ),
    url(r'^estado/$', EstadoSala, name="EstadoSala" ),

    # url(r'^videos/$', VideosListView.as_view(), name="VideosList" ),
    # url(r'^videos/crear/$', VideoCreateView.as_view(), name="VideosCreate" ),
    # url(r'^videos/editar/(?P<pk>[\w-]+)/$', VideoUpdateView.as_view(), name="VideosEdit" ),

    # url(r'^noticias/$', NoticiasListView.as_view(), name="NoticiasList" ),
    # url(r'^noticias/crear/$', NoticiaCreateView.as_view(), name="NoticiaCreate" ),
    # url(r'^noticias/editar/(?P<pk>[\w-]+)/$', NoticiaUpdateView.as_view(), name="VideosEdit" ),

]