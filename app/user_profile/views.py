# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import  PasswordChangeForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

#CONTAR REGISTROS
#from django.db.models import Count
#co =  User.objects.annotate(cont = Count('pk'))
#print co[0].cont



from random import choice

longitud = 6
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

from .forms import *

class IndexView(TemplateView):
    template_name='login.html'



def LoginDef(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                profile = UserProfile.objects.get(user_id=user.pk)
                if profile.fallidos == 3:
                    titulo = 'Recuperar Clave de Usuario'
                    msj = 'Saludos Gracias por utilizar los servicios de ' + settings.SITIO + ', Su Usuario: clave:   El equipo de ' + settings.SITIO + ' Gracias' 
                    html = '<table style="width:600px;margin:auto"><tr> <td style="background:#eeeeee"><p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de <a href="http://' + settings.SITIO + '">' + settings.SITIO + '</a>:<br><b>Usuario:</b> ' + user.username + '<br>se encuentra bloqueado por 3 intentos fallidos de logueo</b> visite el siguiente enlace para desbloquiar su usaurio: <br> <br><a href="http://' + settings.SITIO + '/desbloqueo-usuario/' + str(user.pk) + '/">Desbloquear usuario en ' + settings.SITIO + '</a> <br><br>  El equipo de <b>' + settings.SITIO + '</b> Gracias         </p>        </td>   </tr></table>'
                    EnviarEmailDef(titulo,msj,html,user.email)
                    return HttpResponse('Usuario bloqueado por intentos fallidos. Revise su email')

                login(request, user)
                profile.fallidos=0
                profile.save()
                return HttpResponse('ok')
            else:
                return HttpResponse('Cuante Inactiva')
        else:
            try:
                user = User.objects.get(username=username)
                profile = UserProfile.objects.get(user_id=user.pk)
                if profile.fallidos == 3:
                    titulo = 'Recuperar Clave de Usuario'
                    msj = 'Saludos Gracias por utilizar los servicios de ' + settings.SITIO + ', Su Usuario: clave:   El equipo de ' + settings.SITIO + ' Gracias' 
                    html = '<table style="width:600px;margin:auto"><tr> <td style="background:#eeeeee"><p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de <a href="http://' + settings.SITIO + '">' + settings.SITIO + '</a>:<br><b>Usuario:</b> ' + user.username + '<br>se encuentra bloqueado por 3 intentos fallidos de logueo</b> visite el siguiente enlace para desbloquiar su usaurio: <br> <br><a href="http://' + settings.SITIO + '/desbloqueo-usuario/' + str(user.pk) + '/">Desbloquear usuario en ' + settings.SITIO + '</a> <br><br>  El equipo de <b>' + settings.SITIO + '</b> Gracias         </p>        </td>   </tr></table>'
                    EnviarEmailDef(titulo,msj,html,user.email)
                    return HttpResponse('Usuario bloqueado por intentos fallidos. Revise su email')
                profile.fallidos = profile.fallidos + 1
                profile.save()
            except ObjectDoesNotExist:
                pass

            return HttpResponse('Usuario o password incorrectos') 
    else:
        raise Http404



class ListUsuariosView(ListView):
    model = User
    paginate_by = 5
    template_name = 'listarUsuarios.html'
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ListUsuariosView, self).dispatch(*args, **kwargs)
    def get_queryset(self):
        return User.objects.all().order_by('id')


class UsuarioCreateView(CreateView):
    form_class = UsuarioForm
    template_name = "crearUsuario.html"
    success_url="/usuario/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(UsuarioCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            usuario = User.objects.get(email=request.POST['email'])
            return HttpResponse('existeEmail')
        except ObjectDoesNotExist:
            pass
        try:
            usuario = User.objects.get(username=request.POST['username'])
            return HttpResponse('existeUser')
        except ObjectDoesNotExist:
            usuario = User.objects.create(username=request.POST['username'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
            try:            
                s = Sala.objects.get(pk=request.POST['sala'])                
                profile  = UserProfile.objects.create(user_id=usuario.id,sala=s,telefono=request.POST['telefono'],thumb=request.FILES['file'])            
            except MultiValueDictKeyError:
                profile  = UserProfile.objects.create(user_id=usuario.id,sala=s,telefono=request.POST['telefono'])            

            p = ""
            p = p.join([choice(valores) for i in range(longitud)])
            print p
            usuario.password = make_password(p)    
            usuario.save()
            titulo = 'Usuario Creado'
            msj = 'Saludos Gracias por utilizar los servicios de ' + settings.SITIO + ', Su Usuario:' + usuario.username + ' clave: ' + p + '  El equipo de ' + settings.SITIO + ' Gracias' 
            html = '<table style="width:600px;margin:auto"><tr> <td style="background:#eeeeee"><p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de <a href="http://' + settings.SITIO + '">' + settings.SITIO + '</a>:<br><b>Usuario:</b> ' + usuario.username + '<br><b>Clave:</b> ' + p + '<br><br><br>  El equipo de <b>' + settings.SITIO + '</b> Gracias         </p>        </td>   </tr></table>'
            EnviarEmailDef(titulo,msj,html,usuario.email)

            return HttpResponse('ok')
        return super(UsuarioCreateView, self).post(request,*args, **kwargs)



class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = "editarUsuario.html"
    success_url="/usuarios/"
    def telefono(self,*args,**kwargs):
        p = UserProfile.objects.get(user_id=self.kwargs['pk'])
        return p.telefono
    def sala(self,*args,**kwargs):
        p = UserProfile.objects.get(user_id=self.kwargs['pk'])
        return p.sala.id
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(UsuarioUpdateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        u = User.objects.get(pk=self.kwargs['pk'])
        u.first_name = request.POST['first_name']
        u.last_name = request.POST['last_name']
        u.email = request.POST['email']
        u.save()
        try:
            up = UserProfile.objects.get(user_id=request.POST['id'])
            s = Sala.objects.get(pk=request.POST['sala'])            
            up.sala = s
            up.telefono = request.POST['telefono']
            up.thumb = request.FILES['file']
            up.save()
            
        except MultiValueDictKeyError:
            up = UserProfile.objects.filter(user_id=self.request.POST['id']).update(sala=request.POST['sala'],telefono=request.POST['telefono'],)
        return HttpResponse('ok')


class UsuarioDeleteView(DeleteView):
    model = User
    success_url = "/usuario/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(UsuarioDeleteView, self).dispatch(*args, **kwargs)
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            user = User.objects.get(pk=request.POST['pk'])
            user.delete()
            return HttpResponse('ok')
        else:
            raise Http404




# def RegistroDef(request):
#     if request.is_ajax():
#         Rname = request.POST.get('Rname')
#         Rusername = request.POST.get('Rusername')
#         Remail = request.POST.get('Remail')
#         Rpassword = request.POST.get('Rpassword')
#         try:
#             user = User.objects.get(username=Rusername)
#             msj='existeUser'
#             return HttpResponse(msj)            
#         except ObjectDoesNotExist:
#             try:
#                 user = User.objects.get(email=Remail)
#                 msj='existeEmail'
#                 return HttpResponse(msj)
#             except ObjectDoesNotExist:
#                 pass
#             # E instanciamos un objeto User, con el username y password
#             user_model = User.objects.create_user(username=Rusername, password=Rpassword)
#             # Añadimos el email
#             user_model.email = Remail
#             user_model.first_name= Rname
#             # Y guardamos el objeto, esto guardara los datos en la db.
#             user_model.save()
#             # Ahora, creamos un objeto UserProfile, aunque no haya incluido
#             # una imagen, ya quedara la referencia creada en la db.
#             user_profile = UserProfile()
#             # Al campo user le asignamos el objeto user_model
#             user_profile.user = user_model
#             # y le asignamos la photo (el campo, permite datos null)
#             #user_profile.photo = photo
#             # Por ultimo, guardamos tambien el objeto UserProfile
#             user_profile.save()
        
#             user = authenticate(username=Rusername, password=Rpassword)
#             AsignarDef(user.id)
#             titulo = 'Almorir.me verficacion de email'
#             msj = 'Saludos Gracias por utilizar los servicios de mensajeria post mortem de Almorir.me, en este momento su emnil no esta verificado de click en esiguente vinculo para verficar su email: Verificar email en Almorir.me  El equipo de radiowebdigital.com Gracias'
#             html = '<table style="width:600px;margin:auto"> <tr><td align="center" style="text-align:center;"><img src="http://almorir.me/static/img/logo250.png" alt="">      </td>   </tr>   <tr>        <td style="background:#ccc">            <p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de mensajería post mortem de <a href="http://almorir.me"> Almorir.me</a>, en este momento su <b>email no esta verificado</b> visite el siguiente enlace para verificar su email: <br> <br><a href="http://almorir.me/verificar-email/' + str(request.user.id) + '/">Verificar email en Almorir.me</a> <br><br>  El equipo de <b>Almorir.me</b> Gracias         </p>        </td>   </tr></table>'
#             EnviarEmailDef.apply_async((titulo,msj, html, Remail),countdown=10)
#             login(request, user)
#             return HttpResponse('ok')
#     else:
#         raise Http404

def CheckUserDef(request,username):
    if request.is_ajax():
        try:
            user = User.objects.get(username=username)
            return HttpResponse('existeUser')
        except ObjectDoesNotExist:
            return HttpResponse('ok')
    raise Http404
   
def CheckEmailDef(request,email):
    if request.is_ajax():
        try:
            user = User.objects.get(email=email)
            return HttpResponse('existeEmail')
        except ObjectDoesNotExist:
            return HttpResponse('ok')
    raise Http404
   




@login_required(login_url='/oops/')
def account(request):
    error = None
    name_message = password_message = email_message = ''
    change_name_form = ChangeNameForm(data=request.POST or None, instance=request.user)
    change_password_form = PasswordChangeForm(data=request.POST or None, user = request.user)
    change_email_form = ChangeEmailForm(data=request.POST or None, instance=request.user)
    if request.method == "POST":
    	if "change_name" in request.POST:
    		change_name_form = ChangeNameForm(data=request.POST, instance=request.user)
    		if change_name_form.is_valid():
    			change_name_form.save()
    			name_message = 'Se ha cambiado el nombre satisfactoriamente.'
    	else:
    		change_name_form = ChangeNameForm(instance=request.user)

    	if "change_password" in request.POST:
    		change_password_form = PasswordChangeForm(user=request.user)
    		if change_password_form.is_valid():
    			change_password_form.save()        
    			password_message = 'Your password has been changed.'
    	else:
    		change_password_form = PasswordChangeForm(user=request.user)

    	if "change_email" in request.POST:
            change_email_form = ChangeEmailForm(request.POST, instance=request.user)
            if change_email_form.is_valid():
                try:
                    user = User.objects.get(email=request.POST['email'])
                    if user:
                        email_message = 'El Email se encuentra registrado, no cambio'
                except ObjectDoesNotExist:
                    change_email_form.save()
                    email_message = 'El Email se ha cambiado satisfactoriamente.'
                    titulo = 'Cambio de Email'
                    msj = 'Saludos Gracias por utilizar los servicios de ' + settings.SITIO + ', Su Email principal cambio con exito:' 
                    html = '<table style="width:600px;margin:auto"><tr> <td style="background:#eeeeee"><p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de <a href="http://' + settings.SITIO + '">' + settings.SITIO + '</a>:<br><b>Su Email cambio con exito<br><br><br>  El equipo de <b>' + settings.SITIO + '</b> Gracias         </p>        </td>   </tr></table>'
                    EnviarEmailDef(titulo,msj,html,request.POST['email'])
                
    	else:
    		change_email_form = ChangeEmailForm(instance=request.user)
    return render(request,'account.html', 
                       {'change_name_form': change_name_form,
                        'change_email_form': change_email_form, 
                        'change_password_form': change_password_form,
                        'password_message': password_message,
                        'name_message': name_message,
                        'email_message': email_message,})

def Desbloqueo(request,nano):
    try:
        profile = UserProfile.objects.get(user_id=nano)
        if  profile.fallidos  == 3:
            profile.fallidos = 0
            profile.save()
        else:
            raise Http404
        return render(request,'desbloqueo.html')
    except ObjectDoesNotExist:
        raise Http404



def EnviarEmailDef(titulo,msj,html,email):
    subject, from_email, to = titulo, 'Bingos Marvel<jbroges@gmail.com>', email 
    msg = EmailMultiAlternatives(subject, msj, from_email, [to])
    msg.attach_alternative(html, "text/html")
    msg.send()

