from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^salas/$', RepotSalaView.as_view(), name="SalaRepote" ),
    url(r'^premios/$', RepotpremioView.as_view(), name="RepotpremioView" ),
    url(r'^salas1/$', ReportSalaListView.as_view(), name="SalaRepote1" ),
    url(r'^salas2/$', generar_pdf, name="generar_pdf" ),
    url(r'^cartones/(?P<id>[\w-]+)/$', ReportePCartones, name="ReportePCartones" ),
    url(r'^partida/$', ReportePartida, name="ReportePartida" ),
    url(r'^premios1/$', ReportePremios, name="ReportePremios" ),
    url(r'^cartones-partida/$', combinacionCartones, name="combinacionCartones" ),
    url(r'^combinacion/$', CombinacionView.as_view(), name="CombinacionView" ),
    url(r'^imprimir/(?P<id>[\w-]+)/$', ImprimirCartones, name="Imprimir" ),
    url(r'^imprimir-blank/(?P<id>[\w-]+)/$', ImprimirCartonesBlank, name="Imprimir" ),

    url(r'^genrear-excel-partidas/$', ReportePartidasExcel.as_view(), name="ReportePartidasExcel" ),
    url(r'^formato-excel-partidas/$', MoeloPartida.as_view(), name="MoeloPartida" ),

]