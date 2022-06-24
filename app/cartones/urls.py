from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^asignacion/$', AsigListView.as_view(), name="AsigListView" ),
    url(r'^asignacion/crear/$', AsigCreateView.as_view(), name="AsigCreateView" ),
    url(r'^asignacion/anular/$', AnularCreateView.as_view(), name="AnularCreateView" ),
    url(r'^asignacion/codigo/$', CodigoCreateView.as_view(), name="CodigoCreateView" ),
    url(r'^asignacion/codigo1/$', Codigo, name="CodigoCreateView" ),
    url(r'^asignacion/editar/(?P<pk>[\w-]+)/$', AsigUpdateView.as_view(), name="AsigEdit" ),
    url(r'^asignacion/eliminar/(?P<pk>[-\w]+)/$', AsigDeleteView.as_view(), name="AsigDeleteView" ),
    url(r'^asignacion/generar-de-excel/$', GenerarAsigExcel, name="GenerarAsigExcel" ),

    #url(r'^tikect/$', tikect, name="tikect" ),
    url(r'^imprimir/$', Imprimir.as_view(), name="Imprimir" ),
    url(r'^ganador/$', ganadores, name="ganadores" ),
    url(r'^mostrar-ganador/$', ganador, name="ganador" ),
    url(r'^mostrar-no-ganador/$', Noganador, name="noganador" ),
   

]