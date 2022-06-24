from django.conf.urls import  include, url
from .views import *


urlpatterns = [
    url(r'^en-linea/', ChatEnLinea.as_view(), name="chatenlinea" ),
    url(r'^escribir/', EscribirChat, name="EscribirChat" ),
   	
]