"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler400, handler403, handler404, handler500

from django.contrib import admin
from home.views import *
from cartones.views import *
from configuracion.views import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from user_profile.views import Desbloqueo, account
def handler404(request):
    response = render(request,'404.html', {'a':'aaaaaa'},)
    response.status_code = 404
    return response

def handler500(request):
    response = render(request,'500.html', {},)
    response.status_code = 500
    return response

def LogoutDef(request):
    logout(request)
    return redirect('/')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xls/(?P<nee>\w+)/$', xls),
    url(r'^usuario/', include('user_profile.urls',namespace='userLogin')),
    url(r'^salas/', include('salas.urls',namespace='salas')),
    url(r'^carton/', include('cartones.urls',namespace='salas')),
    url(r'^partida/', include('partidas.urls',namespace='partidas')),
    url(r'^reportes/', include('reportes.urls',namespace='partidas')),
    url(r'^cliente/', include('clientes.urls',namespace='clientes')),
    url(r'^chat/', include('chat.urls',namespace='chat')),
    url(r'^configuracion/(?P<pk>[\w-]+)/$', ConfigUpdateView.as_view(), name="ConfigUpdateView" ),

    #URLS BASES
    url(r'^app/$', Index.as_view(), name='Dashboard' ),
    url(r'^salir/$', LogoutDef, name='salir' ),
 

    #URLS INICIO
    url(r'^$', LoginInt.as_view(), name='LoginInt' ),

    #PASSWORD RESET
    url(r'^password_reset/$',password_reset, {'template_name':'password_reset_form.html','email_template_name':'password_reset_email.html' }, name="password_reset"),
    url(r'^password_reset_done/$', password_reset_done, {'template_name':'password_reset_done.html', }, name="password_reset_done"),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name' : 'password_reset_confirm.html',}, name ='password_reset_confirm'),
    url(r'^password_reset_complete/$', password_reset_complete, {'template_name':'password_reset_complete.html', }, name="password_reset_complete"),

    #DESBLOQUEO DE USUARIO POR INTNTOS FALLIDOS DE LOGIN
    url(r'^desbloqueo-usuario/(?P<nano>[\w-]+)/$', Desbloqueo, name="desbloqueo"),

    #CUENTA DE PERFIL
    url(r'^account/$', account, name="account" ),

]