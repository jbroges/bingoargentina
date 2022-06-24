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

# from .forms import *
from .models import *
from .forms import *
from cartones.models import *
from configuracion.models import *
import time
from datetime import datetime
import xlrd

# Create your views here.


# class SalasListView(ListView):
#     model = Sala
#     template_name='salaslist.html'
#     paginate_by = 5
    
class PartidaCreateView(CreateView):
    form_class = PartidaForm
    template_name = "crearpartida.html"
    success_url="/salas/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(PartidaCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        if request.POST.get('premio_1') == 'true':
            premio_1 = True
        else:
            premio_1 = False
        if request.POST.get('premio_2') == 'true':
            premio_2 = True
        else:
            premio_2 = False
        if request.POST.get('premio_3') == 'true':
            premio_3 = True
        else:
            premio_3 = False
        if request.POST.get('premio_4') == 'true':
            premio_4 = True
        else:
            premio_4 = False
        if request.POST.get('premio_5') == 'true':
            premio_5 = True
        else:
            premio_5 = False
        
        if request.POST.get('premio_6') == 'true':
            premio_6 = True
        else:
            premio_6 = False
        
        if request.POST.get('premio_7') == 'true':
            premio_7 = True
        else:
            premio_7 = False
        
        dt = datetime.strptime(request.POST['fecha'] + " 00:00", "%m/%d/%Y %H:%M")
        try:
            partida = Partida.objects.create(fecha = dt,organiza = request.POST['organiza'], sorteo =  request.POST['sorteo'], precio =  request.POST['precio'], premio_1 = premio_1, monto_1 =  request.POST['monto_1'], premio_2 = premio_2, monto_2 =  request.POST['monto_2'], premio_3 = premio_3, monto_3 =  request.POST['monto_3'], premio_4 = premio_4, monto_4 =  request.POST['monto_4'], premio_5 = premio_5, monto_5 =  request.POST['monto_5'], premio_6 = premio_6, monto_6 =  request.POST['monto_6'], premio_7 = premio_7, monto_7 =  request.POST['monto_7'],thumb = request.FILES['thumb'], transmite =  request.POST['transmite'], condiciones = request.POST['condiciones'], t1f = request.POST['t1f'],t1l = request.POST['t1l'], t2f = request.POST['t2f'],t2l = request.POST['t2l'], t3f = request.POST['t3f'],t3l = request.POST['t3l'],lineasEnJuego = request.POST['lineasEnJuego'], cartonBlank = request.POST['cartonBlank'])
        except MultiValueDictKeyError:
            print "error dado"
            partida = Partida.objects.create(fecha = dt,organiza = request.POST['organiza'], sorteo =  request.POST['sorteo'], precio =  request.POST['precio'], premio_1 = premio_1, monto_1 =  request.POST['monto_1'], premio_2 = premio_2, monto_2 =  request.POST['monto_2'], premio_3 = premio_3, monto_3 =  request.POST['monto_3'], premio_4 = premio_4, monto_4 =  request.POST['monto_4'], premio_5 = premio_5, monto_5 =  request.POST['monto_5'], premio_6 = premio_6, monto_6 =  request.POST['monto_6'], premio_7 = premio_7, monto_7 =  request.POST['monto_7'], transmite =  request.POST['transmite'], condiciones = request.POST['condiciones'], t1f = request.POST['t1f'],t1l = request.POST['t1l'], t2f = request.POST['t2f'],t2l = request.POST['t2l'], t3f = request.POST['t3f'],t3l = request.POST['t3l'],lineasEnJuego = request.POST['lineasEnJuego'], cartonBlank = request.POST['cartonBlank'])
        return HttpResponse('ok')

    
class PartidaUpdateView(UpdateView):
    model = Partida
    form_class = PartidaForm
    template_name = "editpartida.html"
    success_url="/partida/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(PartidaUpdateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        if request.POST.get('premio_1') == 'true':
            premio_1 = True
        else:
            premio_1 = False
        if request.POST.get('premio_2') == 'true':
            premio_2 = True
        else:
            premio_2 = False
        if request.POST.get('premio_3') == 'true':
            premio_3 = True
        else:
            premio_3 = False
        if request.POST.get('premio_4') == 'true':
            premio_4 = True
        else:
            premio_4 = False
        if request.POST.get('premio_5') == 'true':
            premio_5 = True
        else:
            premio_5 = False
        if request.POST.get('premio_6') == 'true':
            premio_6 = True
            print "ESTA ENTRANDO"
        else:
            premio_6 = False
        if request.POST.get('premio_7') == 'true':
            premio_7 = True
        else:
            premio_7 = False

        dt = datetime.strptime(request.POST['fecha'] + " 00:00", "%m/%d/%Y %H:%M")

        try:
            partida = Partida.objects.filter(pk=request.POST['id']).update(fecha = dt, organiza = request.POST['organiza'], sorteo =  request.POST['sorteo'], precio =  request.POST['precio'], premio_1 = premio_1, monto_1 =  request.POST['monto_1'], premio_2 = premio_2, monto_2 =  request.POST['monto_2'], premio_3 = premio_3, monto_3 =  request.POST['monto_3'], premio_4 = premio_4, monto_4 =  request.POST['monto_4'], premio_5 = premio_5, monto_5 =  request.POST['monto_5'], premio_6 = premio_6, monto_6 =  request.POST['monto_6'], premio_7 = premio_7, monto_7 =  request.POST['monto_7'], transmite =  request.POST['transmite'], condiciones = request.POST['condiciones'], t1f = request.POST['t1f'],t1l = request.POST['t1l'], t2f = request.POST['t2f'],t2l = request.POST['t2l'], t3f = request.POST['t3f'],t3l = request.POST['t3l'],lineasEnJuego = request.POST['lineasEnJuego'], cartonBlank = request.POST['cartonBlank'])
        except MultiValueDictKeyError:
            print 'erroe'
            partida = Partida.objects.filter(pk=request.POST['id']).update(fecha = dt, organiza = request.POST['organiza'], sorteo =  request.POST['sorteo'], precio =  request.POST['precio'], premio_1 = premio_1, monto_1 =  request.POST['monto_1'], premio_2 = premio_2, monto_2 =  request.POST['monto_2'], premio_3 = premio_3, monto_3 =  request.POST['monto_3'], premio_4 = premio_4, monto_4 =  request.POST['monto_4'], premio_5 = premio_5, monto_5 =  request.POST['monto_5'], premio_6 = premio_6, monto_6 =  request.POST['monto_6'], premio_7 = premio_7, monto_7 =  request.POST['monto_7'], transmite =  request.POST['transmite'], condiciones = request.POST['condiciones'], t1f = request.POST['t1f'],t1l = request.POST['t1l'], t2f = request.POST['t2f'],t2l = request.POST['t2l'], t3f = request.POST['t3f'],t3l = request.POST['t3l'],lineasEnJuego = request.POST['lineasEnJuego'], cartonBlank = request.POST['cartonBlank'])
        return HttpResponse('ok')


class PartidaListView(ListView):
    model = Partida
    template_name='partidas.html'
    parametro = time.strftime("%Y-%m-%d")
    dia = time.strftime("%Y-%m-%d")
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        self.parametro = time.strftime("%Y-%m-%d")
        self.dia = time.strftime("%m/%d/%Y")
        return super(PartidaListView, self).dispatch(*args, **kwargs)
    def post(self,request,*args,**kwargs):
        self.parametro = datetime.strptime(request.POST['diaBus'] , "%m/%d/%Y")
        self.dia = request.POST['diaBus'] 
        return super(PartidaListView, self).get(request,*args, **kwargs)
    def get_queryset(self):
        return Partida.objects.filter(fecha = self.parametro)  
    def dia(self):
        return self.dia

class PartidaDeleteView(DeleteView):
    model = Partida
    success_url = "/partida/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(PartidaDeleteView, self).dispatch(*args, **kwargs)
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            asig = Partida.objects.get(pk=request.POST['pk'])
            asig.delete()
            return HttpResponse('ok')
        else:
            raise Http404


@login_required(login_url='/')
def crearCartones(request):
    if Impresion.objects.filter(partida_id = int(request.GET['id'])):
        return HttpResponse('Ya Se Generaron Los Cartones Para Esta Partida')    
    cartones = Carton.objects.all()
    num = 0
    for x in sorted(cartones):
        num = num + 1
        print num
        imp = Impresion.objects.create(partida_id = int(request.GET['id']),carton_id = x.id, numeroCarton = num, )
    return HttpResponse('Se Crearon Los Cartones Satisfactoriamente')

@login_required(login_url='/')
def Tablero(request):
    if request.user.userprofile.sala.activa in 'No':
        return render(request,'inactivo.html',{})

    _PREMIO = 'Null'
    balotas = set(range(1,91))
    partida = Partida.objects.filter(id=request.GET['id'])
    if not partida:
        return render(request,'nopartida.html',{})


    if partida[0].premio_1 and not partida[0].ganador_1:
        _PREMIO = "1er Premio"
    
    elif partida[0].premio_2 and not partida[0].ganador_2:
        _PREMIO = "2do Premio"

    elif partida[0].premio_3 and not partida[0].ganador_3:
        _PREMIO = "3er Premio"

    elif partida[0].premio_4 and not partida[0].ganador_4:
       _PREMIO = "4to Premio"

    elif partida[0].premio_5 and not partida[0].ganador_5:
        _PREMIO = "5to Premio"

    elif partida[0].premio_6 and not partida[0].ganador_6:
        _PREMIO = "6to Premio"

    elif partida[0].premio_7 and not partida[0].ganador_7:
        _PREMIO = "7mo Premio"

    jugada = Jugada.objects.filter(partida=partida, premio = _PREMIO)
    
    #define el numero de balotas que han salido
    balotasJugadas = 0
    
    if jugada:
        for j in jugada:
            balotas.remove(int(j.balota))
            balotasJugadas = balotasJugadas + 1

    #cartones en sala
    cartonensala = Impresion.objects.filter(partida_id=partida[0].id,).count()    

    #CARTONES VENDIDOS GENERAL
    cartonvendidos = Impresion.objects.filter(partida_id=partida[0].id,participa='S').count()    
    
    if cartonvendidos == 0:
        return render(request,'novendidos.html',{})

    #SABER SI ES AUTOMATICO O MANUAL SEGUN EL LMODULO CONFIGURACION
    TipoP = Configuracion.objects.get(pk=1)

    if not partida[0].inicio:
        return render(request,'inicio.html',{'TipoP':TipoP.tipopartida,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partida':partida})

    if partida[0].termino:
        return render(request,'termino.html',{})


    #ULTIMAS 5 BALOTAS
    ultimas5 =Jugada.objects.filter(partida=partida, premio = _PREMIO).order_by('-id')[:5]
   

    #SI ES SUPER USER VA AL TABLERO DE ADMIN
    if request.user.is_superuser:
        if TipoP.tipopartida == 'MANUAL':
            if TipoP.theme == 'DARK':
                return render(request,'DarkTableroManual.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id,'f1':partida[0].premio_1,'f2':partida[0].premio_2,'f3':partida[0].premio_3,'f4':partida[0].premio_4,'f5':partida[0].premio_5,'f6':partida[0].premio_6,'f7':partida[0].premio_7,})
            else:
                return render(request,'AdminManual.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id,'f1':partida[0].premio_1,'f2':partida[0].premio_2,'f3':partida[0].premio_3,'f4':partida[0].premio_4,'f5':partida[0].premio_5,'f6':partida[0].premio_6,'f7':partida[0].premio_7,})
        else:
            if TipoP.theme == 'DARK':
                return render(request,'DarkTableroAutoAdmin.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id,'f1':partida[0].premio_1,'f2':partida[0].premio_2,'f3':partida[0].premio_3,'f4':partida[0].premio_4,'f5':partida[0].premio_5,'f6':partida[0].premio_6,'f7':partida[0].premio_7,})
            else:
                return render(request,'tableroAdmin.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id,'f1':partida[0].premio_1,'f2':partida[0].premio_2,'f3':partida[0].premio_3,'f4':partida[0].premio_4,'f5':partida[0].premio_5,'f6':partida[0].premio_6,'f7':partida[0].premio_7,})
    else:
        #TABLERO USUARIO NORMAL
        if TipoP.tipopartida in 'MANUAL':
            if TipoP.theme == 'DARK':
                return render(request,'DarkTableroSalasManual.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id})
            else:
                return render(request,'tableroManual.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id})
        else:
            return render(request,'tablero.html',{'ultimas5':ultimas5,'numeros':jugada,'balotasJugadas':balotasJugadas,'cartonensala':cartonensala,'cartonvendidos':cartonvendidos,'partidanum':partida[0].id})

 
import random
import json
from django.http import JsonResponse

@login_required(login_url='/')
def JuegoSeleccionManualEnLinea(request):
    balotas = set(range(1,91))
    salidos = list()
    _PREMIO = 'Null'

    partida = Partida.objects.filter(id=request.GET['id'])
    print request.GET['id']
    if not partida:
        return render(request,'nopartida.html',{})
    

    if partida[0].premio_1 and not partida[0].ganador_1:
        _PREMIO = "1er Premio"
    
    elif partida[0].premio_2 and not partida[0].ganador_2:
        _PREMIO = "2do Premio"

    elif partida[0].premio_3 and not partida[0].ganador_3:
        _PREMIO = "3er Premio"

    elif partida[0].premio_4 and not partida[0].ganador_4:
       _PREMIO = "4to Premio"

    elif partida[0].premio_5 and not partida[0].ganador_5:
        _PREMIO = "5to Premio"


    elif partida[0].premio_6 and not partida[0].ganador_6:
        _PREMIO = "6to Premio"


    elif partida[0].premio_7 and not partida[0].ganador_7:
        _PREMIO = "7mo Premio"

    #ULTIMAS 5 BALOTAS
    ultimas =Jugada.objects.filter(partida=partida, premio =_PREMIO).order_by('-id')[:5]


    if partida[0].premio_1 == partida[0].ganador_1 and partida[0].premio_2 == partida[0].ganador_2 and partida[0].premio_3 == partida[0].ganador_3 and partida[0].premio_4 == partida[0].ganador_4 and partida[0].premio_5 == partida[0].ganador_5 and partida[0].premio_6 == partida[0].ganador_6 and partida[0].premio_7 == partida[0].ganador_7 :
        param = {'ganador':'termino'}
        partida[0].termino = True
        partida[0].save()
        return JsonResponse(param)
    balotasJugadas=0
    #SACO LAS BALOTAS QUE YA SALIERON DEL ARREGLO O LISTA
    jugada = Jugada.objects.filter(partida=partida, premio =_PREMIO)
    if jugada:
        for j in jugada:
            balotas.remove(int(j.balota))
            salidos.append(int(j.balota))
            balotasJugadas = balotasJugadas + 1
            if balotasJugadas == 90:
                param = {'ganador':'termino'}
                partida[0].termino = True
                partida[0].save()
                return JsonResponse(param)
                
    #SACO LA BALOTA DE LA LISTA
    balota = request.GET['n']
    salidos.append(balota)
    salidos.append(0)
    
    #VALIDO SI NO HAY LA MISMA BALOTA PARA PARTIDA Y GUARDO
    j = Jugada.objects.filter(partida=partida,balota=balota, premio =_PREMIO)
    if not j:
        c = Jugada.objects.create(partida_id=partida[0].id, balota=balota, premio =_PREMIO)  
    

    param = {}
    #PREMIO 1 
    if partida[0].premio_1 == True and partida[0].ganador_1 == False:
        
        if partida[0].ganador_1 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_1 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_1 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_1 = False, participa = 'S')       
        
            print "PREMIO 1"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 1 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_1 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_1 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_1=True
                partida[0].save()
                param = {'ganador':'premio1','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 1 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_1 = 2
                    p.ganador_1 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_1=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio1','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 1 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_1 = 3
                    p.ganador_1 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_1=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio1','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}
    #PREMIO 2 
    elif partida[0].premio_2 == True and partida[0].ganador_2 == False:
        
        if partida[0].ganador_2 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_2 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_2 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_2 = False, participa = 'S')       
        
            print "PREMIO 2"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 2 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_2 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_2 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_2=True
                partida[0].save()
                param = {'ganador':'premio2','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 2 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_2 = 2
                    p.ganador_2 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_2=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio2','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 2 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_2 = 3
                    p.ganador_2 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_2=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio2','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

    #PREMIO 3 
    elif partida[0].premio_3 == True and partida[0].ganador_3 == False:
        
        if partida[0].ganador_3 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_3 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_3 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_3 = False, participa = 'S')       
        
            print "PREMIO 3"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 3 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_3 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_3 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_3=True
                partida[0].save()
                param = {'ganador':'premio3','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 3 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_3 = 2
                    p.ganador_3 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_3=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio3','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 3 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_3 = 3
                    p.ganador_3 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_3=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio3','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}
    #PREMIO 4 
    elif partida[0].premio_4 == True and partida[0].ganador_4 == False:
        
        if partida[0].ganador_4 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_4 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_4 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_4 = False, participa = 'S')       
        
            print "PREMIO 4"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 4 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_4 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_4 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_4=True
                partida[0].save()
                param = {'ganador':'premio4','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 4 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_4 = 2
                    p.ganador_4 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_4=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio4','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 4 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_4 = 3
                    p.ganador_4 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_4=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio4','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

    #PREMIO 5 
    elif partida[0].premio_5 == True and partida[0].ganador_5 == False:
        
        if partida[0].ganador_5 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_5 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_5 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_5 = False, participa = 'S')       
        
            print "PREMIO 5"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 5 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_5 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_5 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_5=True
                partida[0].save()
                param = {'ganador':'premio5','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 5 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_5 = 2
                    p.ganador_5 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_5=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio5','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 5 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_5 = 3
                    p.ganador_5 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_5=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio5','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

    #PREMIO 6 
    elif partida[0].premio_6 == True and partida[0].ganador_6 == False:
        
        if partida[0].ganador_6 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_6 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_6 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_6 = False, participa = 'S')       
        
            print "PREMIO 6"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 6 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_6 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_6 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_6=True
                partida[0].save()
                param = {'ganador':'premio6','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 6 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_6 = 2
                    p.ganador_6 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_6 = True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio6','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 6 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_6 = 3
                    p.ganador_6 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_6 = True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio6','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

    #PREMIO 7 
    elif partida[0].premio_7 == True and partida[0].ganador_7 == False:
        
        if partida[0].ganador_7 == False:
            po = Impresion.objects.filter(partida_id=partida[0].id, carton__l1_1__in=salidos,carton__l1_2__in=salidos,carton__l1_3__in=salidos,carton__l1_4__in=salidos,carton__l1_5__in=salidos,carton__l1_6__in=salidos,carton__l1_7__in=salidos,carton__l1_8__in=salidos,carton__l1_9__in=salidos, ganador_7 = False, participa = 'S')
            po1 = Impresion.objects.filter(partida_id=partida[0].id, carton__l2_1__in=salidos,carton__l2_2__in=salidos,carton__l2_3__in=salidos,carton__l2_4__in=salidos,carton__l2_5__in=salidos,carton__l2_6__in=salidos,carton__l2_7__in=salidos,carton__l2_8__in=salidos,carton__l2_9__in=salidos, ganador_7 = False, participa = 'S')       
            po2 = Impresion.objects.filter(partida_id=partida[0].id, carton__l3_1__in=salidos,carton__l3_2__in=salidos,carton__l3_3__in=salidos,carton__l3_4__in=salidos,carton__l3_5__in=salidos,carton__l3_6__in=salidos,carton__l3_7__in=salidos,carton__l3_8__in=salidos,carton__l3_9__in=salidos,ganador_7 = False, participa = 'S')       
        
            print "PREMIO 7"
            contPosibGanad = 0
            if po:
                for p in po: 
                    print "PREMIO 7 SI LINEA 1"
                    contPosibGanad =  contPosibGanad + 1
                    p.ganador_7 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.linea_7 = 1
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_7=True
                partida[0].save()
                param = {'ganador':'premio7','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po1 and partida[0].lineasEnJuego >= 2:
                for p in po1: 
                    print "PREMIO 7 SI LINEA 2"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_7 = 2
                    p.ganador_7 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_7=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio7','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

            if po2 and partida[0].lineasEnJuego >= 3:
                for p in po2: 
                    print "PREMIO 7 SI LINEA 3"
                    contPosibGanad =  contPosibGanad + 1
                    p.linea_7 = 3
                    p.ganador_7 = True
                    p.ganador = True
                    p.ganador_at = datetime.now()
                    p.save()
                    print "carton numero: ", p.numeroCarton
                partida[0].ganador_7=True
                partida[0].save()
                if not param:
                    param = {'ganador':'premio7','balota':balota,'balotasJugadas':balotasJugadas,'contPosibGanad':contPosibGanad,'FiguraEnJuego':FiguraEnJuego(partida)}

    if not param:
        param = {'ganador':'none','balota':balota,'balotasJugadas':balotasJugadas,'FiguraEnJuego':FiguraEnJuego(partida)}
    return JsonResponse(param)




def FiguraEnJuego(partida):
 
    if partida[0].premio_1 and not partida[0].ganador_1:
        return dict({'tituloFigua':"1er Premio"})
    
    elif partida[0].premio_2 and not partida[0].ganador_2:
        return dict({'tituloFigua':"2do Premio"})

    elif partida[0].premio_3 and not partida[0].ganador_3:
        return dict({'tituloFigua':"3er Premio"})

    elif partida[0].premio_4 and not partida[0].ganador_4:
        return dict({'tituloFigua':"4to Premio"})

    elif partida[0].premio_5 and not partida[0].ganador_5:
        return dict({'tituloFigua':"5to Premio"})

    elif partida[0].premio_6 and not partida[0].ganador_6:
        return dict({'tituloFigua':"6to Premio"})

    elif partida[0].premio_7 and not partida[0].ganador_7:
        return dict({'tituloFigua':"7mo Premio"})

    return dict({'tituloFigua':"En Espera..."})


@login_required(login_url='/')
def inicarPartida(request):

    partida = Partida.objects.filter(pk=request.GET['id']).update(inicio=True)
    return HttpResponse('ok')


@login_required(login_url='/')
def PosiblesGanadores(request):

    partida =Partida.objects.filter(pk=request.GET['id'])
    
    g1 = Impresion.objects.filter(partida_id=partida[0].id, ganador_1 = True).count()

    g2 = Impresion.objects.filter(partida_id=partida[0].id, ganador_2 = True).count()
    
    g3 = Impresion.objects.filter(partida_id=partida[0].id, ganador_3 = True).count()

    g4 = Impresion.objects.filter(partida_id=partida[0].id, ganador_4 = True).count()
    
    g5 = Impresion.objects.filter(partida_id=partida[0].id, ganador_5 = True).count()

    g6 = Impresion.objects.filter(partida_id=partida[0].id, ganador_6 = True).count()

    g7 = Impresion.objects.filter(partida_id=partida[0].id, ganador_7 = True).count()
  
    ganadores = {'g1':g1, 'g2':g2, 'g3':g3, 'g4':g4, 'g5':g5, 'g6':g6, 'g7':g7,}
    partidasFigura = {'premio_1':partida[0].premio_1,'premio_2':partida[0].premio_2,'premio_3':partida[0].premio_3,'premio_4':partida[0].premio_4,'premio_5':partida[0].premio_5,'premio_6':partida[0].premio_6,'premio_7':partida[0].premio_7,}
    return JsonResponse({'ganadores': ganadores, 'partidas':partidasFigura})

@login_required(login_url='/')
def MarcarGanador(request):
    carton = Impresion.objects.get(pk=request.GET['id'])
    partida = Partida.objects.get(pk=carton.partida_id)
    act = Impresion.objects.all().order_by('-id')[:1]
    
    if  carton.partida_id != act[0].partida_id:
        return HttpResponse('fue')

    if request.GET['figura'] == 'LA':
        carton.ganador_8 = True
        partida.ganador_8 = True

    if request.GET['figura'] == 'L1':
        carton.ganador_1 = True
        partida.ganador_1 = True

    if request.GET['figura'] == 'L2':
        carton.ganador_4 = True
        partida.ganador_4 = True
    
    if request.GET['figura'] == 'L3':
        carton.ganador_6 = True
        partida.ganador_6 = True
    
    if request.GET['figura'] == 'L1-L2':
        carton.ganador_2 = True
        partida.ganador_2 = True
    
    if request.GET['figura'] == 'L1-L3':
        carton.ganador_3 = True
        partida.ganador_3 = True
    
    if request.GET['figura'] == 'L2-L3':
        carton.ganador_5 = True
        partida.ganador_5 = True
    
    if request.GET['figura'] == 'casa':
        carton.ganador_7 = True
        partida.ganador_7 = True
    
    if request.GET['figura'] == 'rebingo':
        carton.ganador_9 = True
        partida.ganador_9 = True
    
    if request.GET['figura'] == 'revancha':
        carton.ganador_10 = True
        partida.ganador_10 = True
    
    carton.ganador = True
    carton.ganador_at = time.strftime("%Y-%m-%d")
    carton.save()
    partida.save()
    return HttpResponse('ok')

@login_required(login_url='/')
def GenerarPartidasExcel(request):
    if request.user.is_superuser:
        if request.POST:
            if request.FILES['file']:
                config = Configuracion.objects.get(pk=1)
                config.partida = request.FILES['file']
                config.save()
                xls = '/opt/Bingo/media_files/' + str(config.partida)
                workbook = xlrd.open_workbook(xls)
                sheet = workbook.sheet_by_index(0)
                for i in range(sheet.nrows - 1):
                    c = Partida.objects.create(fecha = str(sheet.cell_value(i+1,0)),descripcion = str(sheet.cell_value(i+1,1)), premio_1 = int(sheet.cell_value(i+1,2)),premio_2 = int(sheet.cell_value(i+1,3)),premio_3 = int(sheet.cell_value(i+1,4)),premio_4 = int(sheet.cell_value(i+1,5)),premio_5 = int(sheet.cell_value(i+1,6)),figura_6 = int(sheet.cell_value(i+1,7)),figura_7 = int(sheet.cell_value(i+1,8)),figura_8 = int(sheet.cell_value(i+1,9)),figura_9 = int(sheet.cell_value(i+1,10)),premio_10 = int(sheet.cell_value(i+1,11)))
                return HttpResponse('ok')

    else:
        raise Http404

@login_required(login_url='/')
def Ultimas5(request):
    partida =Partida.objects.filter(pk=request.GET['id'])
    _PREMIO = 'Null'
    if partida[0].premio_1 and not partida[0].ganador_1:
        _PREMIO = "1er Premio"
    
    elif partida[0].premio_2 and not partida[0].ganador_2:
        _PREMIO = "2do Premio"

    elif partida[0].premio_3 and not partida[0].ganador_3:
        _PREMIO = "3er Premio"

    elif partida[0].premio_4 and not partida[0].ganador_4:
       _PREMIO = "4to Premio"

    elif partida[0].premio_5 and not partida[0].ganador_5:
        _PREMIO = "5to Premio"

    elif partida[0].premio_6 and not partida[0].ganador_6:
        _PREMIO = "6to Premio"

    elif partida[0].premio_7 and not partida[0].ganador_7:
        _PREMIO = "7mo Premio"

    #ULTIMAS 5 BALOTAS
    ultimas5 =Jugada.objects.filter(partida=partida,premio = _PREMIO).order_by('-id')[:5]
    return render(request,'ultimasbalotas.html',{'ultimas5':ultimas5})

@login_required(login_url="/")
def TerminarPartida(request):
    print request.GET['id']
    partida = Partida.objects.filter(pk=request.GET['id']).update(termino=True)    
    return HttpResponse('ok')
