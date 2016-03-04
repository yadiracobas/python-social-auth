# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group, Permission
from models import User

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserForm(forms.ModelForm):

	username = forms.CharField(label= '', 
								widget=forms.TextInput(
													attrs={'class' : 'form-control', 
															'placeholder': 'Nombre de usuario *'}))
	
	email = forms.EmailField(label = '',
							widget=forms.TextInput(
													attrs={'class' : 'form-control', 
															'placeholder':'Correo electrónico *'}))
	
	password_one = forms.CharField(label= '',
									widget=forms.PasswordInput(
															render_value=False, 
															attrs={'class' : 'form-control',
																	'placeholder': 'Contraseña *'}))
	
	password_two = forms.CharField(label= '',
									widget=forms.PasswordInput(
															render_value=False, 
															attrs={'class' : 'form-control',
															'placeholder': 'Repetir contraseña *'}))
	
	first_name = forms.CharField(label= '',
								widget=forms.TextInput(
														attrs={'class' : 'form-control',
														'placeholder': 'Nombre *'}))
	
	last_name = forms.CharField(label= '',
								widget=forms.TextInput(
														attrs={'class' : 'form-control',
														'placeholder':'Apellido paterno *'}))
	
	last_mom_name = forms.CharField(label= '',
									required = False, 
									widget=forms.TextInput(
															attrs={'class' : 'form-control',
															'placeholder': 'Apellido materno'}))
	
	gender_opts = ( ('M', 'Masculino'), ('F', 'Femenino'), )
	gender = forms.CharField(label = 'Género',
							required = False,
							widget=forms.Select(choices=gender_opts))

	mobile_no = forms.CharField(label = 'Número de teléfono',
								required = False,
								help_text = 'Debe incluir Número de ciudad y estado',
								widget=forms.TextInput(attrs={'class' : 'form-control',
															'placeholder': 'Teléfono',
															'type': 'number',}))
	
	date_of_birth = forms.DateField(label = 'Fecha de nacimiento',
									required=False,
									widget=forms.DateInput(attrs={'class': 'form-control',
															'type': 'date'}))
	
	avatar = forms.ImageField(label= 'Imagen de perfil',
							required=False,
							widget=forms.FileInput(
												attrs={'class':'filestyle',
														'data-buttonText':"Subir imagen",
														'data-icon':"false"}))

	is_superuser = forms.BooleanField(label = 'Es superusuario',
										required = False,
								help_text = 'Indica que este usuario posee todos los permisos sin que sea necesario asignarle los mismos en forma explícita.',
								widget = forms.CheckboxInput())

	is_staff = forms.BooleanField(label = 'Es staff',
								required = False,
								help_text = 'Indica si el usuario puede ingresar a este sitio de administración.',
								widget = forms.CheckboxInput())

	is_active = forms.BooleanField(label = 'Activo',
								help_text = 'Indica si el usuario debe ser tratado como un usuario activo. Desactive este campo en lugar de eliminar usuarios.',
								initial=True,
								required = False,
								widget = forms.CheckboxInput(attrs={
																	'checked' : 'checked',
															}))
	groups = forms.ModelMultipleChoiceField(label = 'Grupos',
											help_text = 'Mantenga presionada "Control", o "Command" en una Mac, para seleccionar más de uno.',
											required = True,
											queryset = Group.objects.all(),
											widget = forms.SelectMultiple(attrs = {
																					'class':'form-control',
																					'required':'True',
																					}))
	user_permissions = forms.ModelMultipleChoiceField(label = 'Permisos',
											help_text = 'Mantenga presionada "Control", o "Command" en una Mac, para seleccionar más de uno.',
											queryset = Permission.objects.all().exclude(
												content_type__app_label__in=['admin', 'auth', 'contenttypes',
												'django', 'djcelery', 'sessions', 'south',
												]),
											widget = forms.SelectMultiple(attrs = {
																					'class':'form-control',
																					}))
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')	

	class Meta:
		model = User
		fields = [	'username', 'email', 'password_one', 
					'password_two', 'first_name', 'last_name',
					'last_mom_name','gender', 'mobile_no',
					'date_of_birth', 'avatar', ]


class SigninUserForm(forms.ModelForm):

	username = forms.CharField(label= '', 
								widget=forms.TextInput(
													attrs={'class' : 'form-control', 
															'placeholder': 'Nombre de usuario *'}))
	password = forms.CharField(label= '',
									widget=forms.PasswordInput(
															render_value=False, 
															attrs={'class' : 'form-control',
																	'placeholder': 'Contraseña *'}))
	class Meta:
		model = User
		fields = ('username', 'password',)