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
from partidas.models import *
from configuracion.models import *
from clientes.models import *
import time
from datetime import datetime
import xlrd

@login_required(login_url='/')
def xls(request, nee=None):
    print 'entro'
    n = (int(nee)*1000)-1000
    print 'paso 1'
    file = "/opt/Bingo90Arg/app/DBxls.xlsx"
    print 'paso 2'
    workbook = xlrd.open_workbook(file)
    print 'paso 3'
    sheet = workbook.sheet_by_index(0)
    print 'paso 4'
    for i in range(1000):
        print (i+n)+1, "Fila"
        c = Carton.objects.create(l1_1 = str(int(sheet.cell_value(i+n,0))),l1_2 = str(int(sheet.cell_value(i+n,1))), l1_3 = str(int(sheet.cell_value(i+n,2))), l1_4 = str(int(sheet.cell_value(i+n,3))), l1_5 = str(int(sheet.cell_value(i+n,4))), l1_6 = str(int(sheet.cell_value(i+n,5))), l1_7 = str(int(sheet.cell_value(i+n,6))), l1_8 = str(int(sheet.cell_value(i+n,7))), l1_9 = str(int(sheet.cell_value(i+n,8))), l2_1 = str(int(sheet.cell_value(i+n,9))), l2_2 = str(int(sheet.cell_value(i+n,10))), l2_3 = str(int(sheet.cell_value(i+n,11))), l2_4 = str(int(sheet.cell_value(i+n,12))), l2_5 = str(int(sheet.cell_value(i+n,13))), l2_6 = str(int(sheet.cell_value(i+n,14))), l2_7 = str(int(sheet.cell_value(i+n,15))), l2_8 = str(int(sheet.cell_value(i+n,16))), l2_9 = str(int(sheet.cell_value(i+n,17))), l3_1 = str(int(sheet.cell_value(i+n,18))), l3_2 = str(int(sheet.cell_value(i+n,19))), l3_3 = str(int(sheet.cell_value(i+n,20))), l3_4 = str(int(sheet.cell_value(i+n,21))), l3_5 = str(int(sheet.cell_value(i+n,22))), l3_6 = str(int(sheet.cell_value(i+n,23))), l3_7 = str(int(sheet.cell_value(i+n,24))), l3_8 = str(int(sheet.cell_value(i+n,25))), l3_9 = str(int(sheet.cell_value(i+n,26))),)
    return HttpResponse('cojo culo')


# ASIGNACIONES #
class AsigListView(ListView):
    model = Asignacion
    template_name='asignacionlist.html'
    parametro = time.strftime("%Y-%m-%d")
    dia = time.strftime("%Y-%m-%d")
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        self.parametro = time.strftime("%Y-%m-%d")
        self.dia = time.strftime("%m/%d/%Y")
        return super(AsigListView, self).dispatch(*args, **kwargs)
    def post(self,request,*args,**kwargs):
        self.parametro = datetime.strptime(request.POST['diaBus'] , "%m/%d/%Y")
        self.dia = request.POST['diaBus'] 
        return super(AsigListView, self).get(request,*args, **kwargs)
    def get_queryset(self):
        return Asignacion.objects.filter(partida__termino=False)  

class AsigCreateView(CreateView):
    form_class = AsignacionForm
    template_name = "crearasignacion.html"
    success_url="/carton/asignacion/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(AsigCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        c = Asignacion.objects.create(sala_id = request.POST['sala'],partida_id=request.POST['partida'], correlat_ini=request.POST['correlat_ini'], correlat_fin=request.POST['correlat_fin'],)
        for i in range(int(request.POST['correlat_ini']), int(request.POST['correlat_fin']) + 1):
            Impresion.objects.filter(partida_id = request.POST['partida'],numeroCarton=i).update(participa='N')
        return HttpResponse('ok')

class AnularCreateView(CreateView):
    form_class = AsignacionForm
    template_name = "anularCarton.html"
    success_url="/carton/asignacion/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
	print "ACA ESTA EL PEO"
        return super(AnularCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        Impresion.objects.filter(partida_id = request.POST['partida'],numeroCarton=request.POST['numcarton']).update(participa='A')
        return HttpResponse('ok')

class CodigoCreateView(TemplateView):
    template_name = "codigo.html"


def Codigo(request):
    Impresion.objects.filter(id = request.POST['id'],).update(participa='N')
    return HttpResponseRedirect('/carton/asignacion/codigo/')

class AsigUpdateView(UpdateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = "editarAsig.html"
    success_url="/carton/asignacion/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(AsigUpdateView, self).dispatch(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        a = Asignacion.objects.filter(pk=self.kwargs['pk']).update(cantidad = self.request.POST['cantidad'])
        return HttpResponse('ok')

class AsigDeleteView(DeleteView):
    model = Sala
    success_url = "/carton/asignacion/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(AsigDeleteView, self).dispatch(*args, **kwargs)
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            asig = Asignacion.objects.get(pk=request.POST['pk'])
            asig.delete()
            return HttpResponse('ok')
        else:
            raise Http404

# FIN ASIGNACIONES #

# IMPRESIONES #

class Imprimir(TemplateView):
    form_class = ImprimirForm
    template_name='impresiones.html'



@login_required(login_url='/')
def ganadores(request):
    t = None
    try:
        t = request.GET.get('carton','0')
    except MultiValueDictKeyError:
        pass

    if t != '0' and t!= None and t != '':
        imp = Impresion.objects.filter(pk=request.GET['carton'])
        if imp:
            partida = Partida.objects.filter(pk=imp[0].partida_id)[:1]  
     
        else:  
            return render(request,'ganadores.html',{'mensaje':'NoGanador',})

        #BALOTAS JUGADAS PARA MARCAR NUMERO INDIVIDUALMENTE CON 'IN' EN EL TEMPLATE
        j = Jugada.objects.filter(partida=partida)
        balotasJugadas = []
        if j:
            for balota in j:
                balotasJugadas.append(balota.balota)

        ganador = Impresion.objects.filter(pk=request.GET['carton'])      
        if ganador:
            return render(request,'ganadores.html',{'balotasJugadas':balotasJugadas,'obj':ganador,'mensaje':'Ganador de la Partida ','partida':ganador[0].partida_id,'f8':partida[0].ganador_8,'f1':partida[0].ganador_1,'f2':partida[0].ganador_2,'f3':partida[0].ganador_3,'f4':partida[0].ganador_4,'f5':partida[0].ganador_5,'f6':partida[0].ganador_6,'f7':partida[0].ganador_7,'f10':partida[0].ganador_10,'f9':partida[0].ganador_9})
        else:
            return render(request,'ganadores.html',{'mensaje':'NoGanador',})

        if not partida:
            partida = Partida.objects.filter(termino = True).order_by('-id')[:1]
            ganador = Impresion.objects.filter(partida_id = partida[0].id, ganador_1 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_2 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_3 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_4 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_5 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_6 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_7 = True)      
            return render(request,'ganadores.html',{'balotasJugadas':balotasJugadas,'obj':ganador,'mensaje':'Ganadores de la Ultima Partida Jugada','partida':partida[0].id,'f8':partida[0].ganador_8,'f1':partida[0].ganador_1,'f2':partida[0].ganador_2,'f3':partida[0].ganador_3,'f4':partida[0].ganador_4,'f5':partida[0].ganador_5,'f6':partida[0].ganador_6,'f7':partida[0].ganador_7,'f10':partida[0].ganador_10,'f9':partida[0].ganador_9})

    imp = Impresion.objects.all().order_by('-id')[:1]
    partida = Partida.objects.filter(pk=imp[0].partida_id)[:1]  
        
    ganador = Impresion.objects.filter(partida_id = partida[0].id, ganador_1 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_2 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_3 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_4 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_5 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_6 = True) | Impresion.objects.filter(partida_id = partida[0].id, ganador_7 = True)      
    #BALOTAS JUGADAS PARA MARCAR NUMERO INDIVIDUALMENTE CON 'IN' EN EL TEMPLATE
    j = Jugada.objects.filter(partida=partida)
    balotasJugadas = []
    if j:
        for balota in j:
            balotasJugadas.append(balota.balota)

    return render(request,'ganadores.html',{'balotasJugadas':balotasJugadas,'obj':ganador,'mensaje':'Ganadores de la Partida En Curso','partida':partida[0].id,'f8':partida[0].ganador_8,'f1':partida[0].ganador_1,'f2':partida[0].ganador_2,'f3':partida[0].ganador_3,'f4':partida[0].ganador_4,'f5':partida[0].ganador_5,'f6':partida[0].ganador_6,'f7':partida[0].ganador_7,'f10':partida[0].ganador_10,'f9':partida[0].ganador_9})



@login_required(login_url='/')
def Noganador(request):
    print 'carton no  ganador',request.GET.get('carton','0')
    imp = Impresion.objects.all().order_by('-id')[:1]
    partida = Partida.objects.filter(pk=imp[0].partida_id)[:1]  

    carton = Impresion.objects.filter(pk = request.GET.get('carton','0'))
    #BALOTAS JUGADAS PARA MARCAR NUMERO INDIVIDUALMENTE CON 'IN' EN EL TEMPLATE
    j = Jugada.objects.filter(partida=partida)
    balotasJugadas = []
    if j:
        for balota in j:
            balotasJugadas.append(balota.balota)
    return render(request,'cartonNoGanador.html',{'balotasJugadas':balotasJugadas,'carton':carton,})


def ContGanadores(partida):
    return dict({'f8':partida[0].ganador_8})




@login_required(login_url='/')
def ganador(request):
    print request.GET.get('figura','0')
    partida = Partida.objects.filter(id=request.GET['id'])[:1]
    if request.GET.get('figura','0') == 'premio1':
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_1=True)
    elif request.GET.get('figura','0') == 'premio2':
        print "este es " , request.GET.get('figura','0') 
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_2=True)
    elif request.GET.get('figura','0') == 'premio3':
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_3=True)
    elif request.GET.get('figura','0') == 'premio4':
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_4=True)
    elif request.GET.get('figura','0') == 'premio5':
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_5=True)
    elif request.GET.get('figura','0') == 'premio6':
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_6=True)
    elif request.GET.get('figura','0') == 'premio7':
        ganador = Impresion.objects.filter(partida_id=partida[0].id, ganador_7=True)
    if ganador:
        return render(request,'cartonGanador.html',{'obj':ganador,'mensaje':'Ganador de la Partida ','partida':ganador[0].partida_id,})
    return HttpResponse('nada')

   
@login_required(login_url='/')
def GenerarAsigExcel(request):
    if request.user.is_superuser:
        if request.POST:
            if request.FILES['file']:
                config = Configuracion.objects.get(pk=1)
                config.asignaciones = request.FILES['file']
                config.save()
                xls = '/opt/Bingo/media_files/' + str(config.asignaciones)
                workbook = xlrd.open_workbook(xls)
                sheet = workbook.sheet_by_index(0)
                for i in range(sheet.nrows - 1):
                    c = Asignacion.objects.create(partida_id = int(sheet.cell_value(i+1,0)),sala_id = int(sheet.cell_value(i+1,2)),cantidad =  int(sheet.cell_value(i+1,4)))
                return HttpResponse('ok')

    else:
        raise Http404
