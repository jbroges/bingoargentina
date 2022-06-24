# -*- encoding: utf-8 -*-
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
from salas.models import *
from django.http import JsonResponse
# Create your views here.

# ASIGNACIONES #

class ClienteListView(ListView):
    model = Cliente
    template_name ='clientes.html'
    order_by = 10
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ClienteListView, self).dispatch(*args, **kwargs)


class ClienteCreateView(CreateView):
    form_class = ClienteForm
    template_name = "addcliente.html"
    success_url="/cliente/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ClienteCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        print "DNI ", request.user.userprofile.sala
        try:
            cliente = Cliente.objects.get(dni=request.POST['dni'])
            return HttpResponse('existeDNI')
        except ObjectDoesNotExist:
            pass

        try:
            cliente = Cliente.objects.create(nombre = request.POST['nombre'], apellido =  request.POST['apellido'], dni=request.POST['dni'], telefono = request.POST['telefono'], direccion = request.POST['direccion'], sala = self.request.user.userprofile.sala, thumb = request.FILES['file'])
        except MultiValueDictKeyError:
            cliente = Cliente.objects.create(nombre = request.POST['nombre'], apellido =  request.POST['apellido'], dni=request.POST['dni'], telefono = request.POST['telefono'], direccion = request.POST['direccion'], sala = self.request.user.userprofile.sala,)
        return HttpResponse('ok')


class ClienteUpdateiew(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "editcliente.html"
    success_url="/cliente/"

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ClienteUpdateiew, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            print "ERNTRO EDIT CLIENTE"
            c = Cliente.objects.get(pk=self.kwargs['pk'])
            c.nombre = request.POST['nombre']
            c.apellido = request.POST['apellido']
            c.dni = request.POST['dni']
            c.telefono = request.POST['telefono']
            c.thumb = request.FILES['file']
            c.save()
            return HttpResponse('ok')
        except MultiValueDictKeyError:
            up = Cliente.objects.filter(pk = self.kwargs['pk']).update(nombre = request.POST['nombre'], apellido =  request.POST['apellido'], dni=request.POST['dni'], telefono = request.POST['telefono'], direccion = request.POST['direccion'],)
        return HttpResponse('ok')

class ClienteDeleteView(DeleteView):
    print "ENTRO"
    model = Cliente
    success_url = "/cliente/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ClienteDeleteView, self).dispatch(*args, **kwargs)
    def delete(self, request, *args, **kwargs):
        print "delete Entro"
        if request.is_ajax():
            print "ajax Entro"
            cliente = Cliente.objects.get(pk=request.POST['pk'])
            cliente.delete()
            return HttpResponse('ok')
        else:
            raise Http404


@login_required(login_url='/')
def VerificarCliente(request):
    try:
        c = Cliente.objects.get(dni=request.GET['cedula'])
    except ObjectDoesNotExist:
        return HttpResponse('NoExiste')
    return JsonResponse({'nombre':c.nombre,'telefono':c.telefono})