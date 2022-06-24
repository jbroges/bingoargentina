from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from user_profile.models import UserProfile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.utils.datastructures import MultiValueDictKeyError

from .models import *
from .forms import *



class ConfigUpdateView(UpdateView):
    model = Configuracion
    form_class = ConfigForm
    template_name = "config.html"
    success_url="/configuracion/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        c = Configuracion.objects.filter(pk=1)
        if not c:
            a = Configuracion.objects.create(tiempoInter='3000',tiempoMaster='5000')
            a.save()
        return super(ConfigUpdateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            c = Configuracion.objects.get(pk=1)
            c.tiempoMaster = request.POST['tiempoMaster']
            c.tiempoInter = request.POST['tiempoInter']
            c.tipopartida = request.POST['tipopartida']
            c.theme = request.POST['theme']
            c.save()
        except MultiValueDictKeyError:
            pass
        return HttpResponse('ok')
