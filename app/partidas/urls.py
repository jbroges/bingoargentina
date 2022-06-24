from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^$', PartidaListView.as_view(), name="PartidaListView" ),
    url(r'^crear/$', PartidaCreateView.as_view(), name="PartidaCrear" ),
    url(r'^editar/(?P<pk>[\w-]+)/$', PartidaUpdateView.as_view(), name="PartidaUpdateView" ),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', PartidaDeleteView.as_view(), name="PartidaDeleteView" ),


    url(r'^bingo-en-linea/$', Tablero, name="tablero" ),
    url(r'^marcar-carton/$', MarcarGanador, name="MarcarGanador" ),

    url(r'^posibles/$', PosiblesGanadores, name="PosiblesGanadores" ),
    url(r'^jugar-seleccion-manual/$', JuegoSeleccionManualEnLinea, name="JuegoManualEnLinea" ),
    url(r'^iniciar/$', inicarPartida, name="inicarPartida" ),
    url(r'^generar-de-excel/$', GenerarPartidasExcel, name="GenerarPartidasExcel" ),
    url(r'^ultimas5/$', Ultimas5, name="ultimas5" ),
    url(r'^terminar/$', TerminarPartida, name="TerminarPartida" ),
    url(r'^crearCartones/$', crearCartones, name="crearCartones" ),

]