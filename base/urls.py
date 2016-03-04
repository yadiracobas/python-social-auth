from django.conf.urls import include, url
from django.contrib import admin
from userprofiles import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^users/', include('userprofiles.urls', namespace='userprofiles')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
