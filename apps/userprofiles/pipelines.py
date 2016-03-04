# -*- coding: utf-8 -*-
from .models import User 



"""Esto es una funcion pipeline,
para salvar información cuando los usuarios
se autentiquen mediante redes sociales.
permite salvar el sexo, el correo electronico,
y la imagen de perfil"""
def update_user_social_data(backend, strategy, *args, **kwargs):
    
    if not kwargs['is_new']:
        #si ya existe el usuario no hace mas nada
        return
    
    if not kwargs['user']:
        """
            si no se creo el usuario no hace nada,
            esto significa que paso por create_user del modelo User
            y ya existia un usuario con el correo proporcionado
            ejemplo: el usuario se autentico con facebook y gmail y
            dichas cuentas tienen el mismo correo
        """
    	return
    else:
     	user = kwargs['user']
        response =   kwargs['response']    

        if backend.name == 'facebook':
        	if response['gender'] == 'mujer':
        		user.gender = 'F'
        	else:
        		user.gender = 'M'
        	user.email = response['email']
        	avatar = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        
        if backend.name == 'google-oauth2':
        	details = kwargs['details']
        	user.email = details['email']
        	if response['gender'] == 'female':
        		user.gender = 'F'
        	else:
        		user.gender = 'M'
        	avatar = response['image']['url']

        if backend.name == 'twitter':
        	user.email = kwargs['username'] + '@twitter.com'
        	avatar = kwargs['response']['profile_image_url']

        user.save()