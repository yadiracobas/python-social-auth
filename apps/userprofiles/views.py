# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from forms import *


def home(request):	
	return render(request, 'home.html')

def user_login(request):
	errors = ''
	form = SigninUserForm(request.POST or None)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				errors = 'Su usuario no está activado aún'
		else:
			errors = "Nombre de usuario o contraseña inválida"
	ctx = {'form':form,
			'errors': errors,
			}
	return render(request, 'login.html', ctx)

def signout(request):
    logout(request)
    messages.success(request, 'Se ha desconectado con éxito.')
    return redirect(reverse('home'))

"""
-por defecto el nombre del listado es object_list,

-por defecto la ubicación y nombre de la plantilla
	es app_name/nombre en minuscula del modelo en cuestión,
	seguido de _list, Ej: userprofiles/user_list.

-Si se quiere especificar el nombre de la plantilla
	es template_name='templates/listado.html',

-si quiere espedicicar el nombre del objecto
	es context_object_name = 'my_favorite_name'
"""
class UserList(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetail(DetailView):
	model = User
	template_name = 'user_detail.html'

class UserCreate(CreateView):
    model = User
    template_name = 'user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('userprofiles:user_list')

class UserUpdate(UpdateView):
    model = User
    template_name = 'user_update_form.html'
    fields = ['username', 'first_name', 'last_name',
    			'last_mom_name', 'gender', 'mobile_no',
    			'date_of_birth', 'avatar', 'is_admin', 
    			'is_active', 'is_superuser','groups', 
    			'user_permissions']
    success_url = reverse_lazy('userprofiles:user_list')

class UserDelete(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('userprofiles:user_list')

def contact_view(request):

	msg = ''
	error = ''
	if request.method == 'POST':
		contactForm = ContactForm(request.POST)
		if contactForm.is_valid():
			subject = request.POST.get('subject')
			message = request.POST.get('message')
			from_email = request.POST.get('email')
			try:
				send_mail(subject, message, from_email, ['django.cobas@gmail.com'])
				msg = 'Gracias por contactar con nosotros. Enseguida atenderemos su solicitud'
				contactForm = ContactForm()
			except:
				error = 'No se pudo enviar el correo electrónico'
		else:
			error = 'No se pudo enviar la información, revise los datos'
	else:
		contactForm = ContactForm()
	
	ctx = {'contactForm': contactForm,
			'msg': msg,
			'error': error,}
	return render(request, 'contact.html', ctx)

# def update_user_social_data(strategy, *args, **kwargs):
#     """Set the name and avatar for a user only if is new.
#     """
#     print kwargs
#     print 'update_user_social_data ::', strategy
#     if not kwargs['is_new']:
#         return

#     full_name = ''
#     backend = kwargs['backend']
#     user = kwargs['user']


#     if (
#         isinstance(backend, GoogleOAuth2)
#         or isinstance(backend, FacebookOAuth2)
#     ):
#         full_name = kwargs['response'].get('name')
#     elif (
#         isinstance(backend, LinkedinOAuth)
#         or isinstance(backend, TwitterOAuth)
#     ):
#         if kwargs.get('details'):
#             full_name = kwargs['details'].get('fullname')

#     user.full_name = full_name

#     if isinstance(backend, GoogleOAuth2):
#         if response.get('image') and response['image'].get('url'):
#             url = response['image'].get('url')
#             ext = url.split('.')[-1]
#             user.avatar.save(
#                '{0}.{1}'.format('avatar', ext),
#                ContentFile(urllib2.urlopen(url).read()),
#                save=False
#             )
#     elif isinstance(backend, FacebookOAuth2):
#         fbuid = kwargs['response']['id']
#         image_name = 'fb_avatar_%s.jpg' % fbuid
#         image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
#         image_stream = urlopen(image_url)

#         user.avatar.save(
#             image_name,
#             ContentFile(image_stream.read()),
#         )
#     elif isinstance(backend, TwitterOAuth):
#         if kwargs['response'].get('profile_image_url'):
#             image_name = 'tw_avatar_%s.jpg' % full_name
#             image_url = kwargs['response'].get['profile_image_url']
#             image_stream = urlopen(image_url)

#             user.avatar.save(
#                 image_name,
#                 ContentFile(image_stream.read()),
#             )
#     elif isinstance(backend, LinkedinOAuth):
#         if kwargs['response'].get('pictureUrl'):
#             image_name = 'linked_avatar_%s.jpg' % full_name
#             image_url = kwargs['response'].get['pictureUrl']
#             image_stream = urlopen(image_url)

#             user.avatar.save(
#                 image_name,
#                 ContentFile(image_stream.read()),
#             )
#     user.save()


