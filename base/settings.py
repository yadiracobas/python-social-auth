# -*- coding: utf-8 -*-
import os, sys
from unipath import Path


BASE_DIR = Path(__file__).ancestor(2)
sys.path.append(BASE_DIR.child("apps"))

SECRET_KEY = '-*km_4l7$py6mlw1522!r+z(o8p$c!eld$*yp9l&j!df7be9+7'

DEBUG = True

ALLOWED_HOSTS = []


DJANGO_APPS = (
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            )
THIRD_PARTY_APPS = (
                    'social.apps.django_app.default',
                    )

LOCAL_APPS = (
                'userprofiles',
                'social_auth',
            )

INSTALLED_APPS = DJANGO_APPS +  LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS':True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]
WSGI_APPLICATION = 'base.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

AUTH_USER_MODEL = 'userprofiles.User'
