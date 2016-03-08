from django.conf.urls import patterns, include, url
from . import views
from .views import UserList, UserCreate, UserUpdate, UserDelete, UserDetail

urlpatterns = [
	url(r'^login/$', views.user_login, name = 'login'),
	url(r'^signout/$', views.signout, name='signout'),
    url(r'^user_list/$', UserList.as_view(), name = 'user_list'),
    url(r'user/(?P<pk>[0-9]+)/detail/$', UserDetail.as_view(), name='user-detail'),
    url(r'user/add/$', UserCreate.as_view(), name='user-add'),
    url(r'user/(?P<pk>[0-9]+)/$', UserUpdate.as_view(), name='user-update'),
    url(r'user/(?P<pk>[0-9]+)/delete/$', UserDelete.as_view(), name='user-delete'),
    url(r'^contact/$', views.contact_view, name = 'contact'),
]