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

# from .forms import *
from .models import *
from .forms import *

# Create your views here.


class SalasListView(ListView):
    model = Sala
    template_name='salaslist.html'
    paginate_by = 5
    def get_queryset(self):
        return Sala.objects.all().order_by('id')
    
class SalaCreateView(CreateView):
    form_class = SalaForm
    template_name = "crearsala.html"
    success_url="/salas/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(SalaCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            sala = Sala.objects.get(nombre__iexact = request.POST['nombre'])
            if sala:
                return HttpResponse('salaExiste')
        except ObjectDoesNotExist:
            pass
    	try:
            sala = Sala.objects.create(nombre=request.POST['nombre'],direccion=request.POST['direccion'],thumb=request.FILES['file'],)
        except MultiValueDictKeyError:
            sala = Sala.objects.create(nombre=request.POST['nombre'],direccion=request.POST['direccion'],)
    	return HttpResponse('ok')



class SalaUpdateView(UpdateView):
    model = Sala
    form_class = SalaForm
    template_name = "editarsala.html"
    success_url="/salas/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(SalaUpdateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            s = Sala.objects.get(pk=self.kwargs['pk'])
            s.nombre = request.POST['nombre']
            s.direccion = request.POST['direccion']
            s.thumb = request.FILES['file']
            s.save()
        except MultiValueDictKeyError:
            s = Sala.objects.filter(pk=self.kwargs['pk']).update(nombre = request.POST['nombre'],direccion = request.POST['direccion'])
        return HttpResponse('ok')


class SalaDeleteView(DeleteView):
    model = Sala
    success_url = "/salas/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(SalaDeleteView, self).dispatch(*args, **kwargs)
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            sala = Sala.objects.get(pk=request.POST['pk'])
            sala.delete()
            return HttpResponse('ok')
        else:
            raise Http404

def  EstadoSala(request):
    if request.is_ajax():
        sala = Sala.objects.get(pk=request.GET['pk'])
        if sala.activa in 'Si':
            sala.activa = 'No'
            sala.save()
            return HttpResponse('No')
        else:
            sala.activa = 'Si'
            sala.save()
            return HttpResponse('Si')
    else:
        raise Http404
