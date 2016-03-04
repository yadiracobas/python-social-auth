# -*- coding: utf-8 -*-
from .settings import * 


""" Configuracion para la autenticacion con redes sociales """

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email',]

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'

SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# facebook#
SOCIAL_AUTH_FACEBOOK_KEY = '1687750374844001'

SOCIAL_AUTH_FACEBOOK_SECRET = '1be356db8879b36d850759a01606f286'

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'es_MX',
  'fields': 'name, email, gender, birthday' ,
}

#twitter
SOCIAL_AUTH_TWITTER_KEY = 'isvNhRfpgfbCLvxC31cYGAC7f'

SOCIAL_AUTH_TWITTER_SECRET = '39Zm8Kwmc9nQgy6dvhY7HQ3apZK1PnOywPPTp6X2qSzDPAmGRB'

#google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '484760777294-j614c55kufefo2d9g522tmh96c9vopjg.apps.googleusercontent.com'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'j3yNsKb9WHOI46dt3E7ntwwb'

SOCIAL_AUTH_GOOGLE_PROFILE_EXTRA_PARAMS = {
  'locale': 'es_MX',
  'fields': 'name, email, gender, birthday' ,
}

SOCIAL_AUTH_PIPELINE = (
    # recibe vía backend y uid las instancias de social_user y user
    'social.pipeline.social_auth.social_details',

    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',

    # Recibe según user.email la instancia del usuario y lo reemplaza con uno que recibió anteriormente
    'social.pipeline.social_auth.social_user',

    # Trata de crear un username válido según los datos que recibe
    'social.pipeline.user.get_username',

    # Crea un usuario nuevo si uno todavía no existe
    'social.pipeline.user.create_user',

    # Trata de conectar las cuentas
    'social.pipeline.social_auth.associate_user',

    # Recibe y actualiza social_user.extra_data
    'social.pipeline.social_auth.load_extra_data',

    # Actualiza los campos de la instancia user con la información que obtiene vía backend
    'social.pipeline.user.user_details',

    'userprofiles.pipelines.update_user_social_data',
)