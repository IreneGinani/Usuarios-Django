from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^Usuario/new/$', views.user_new, name='user_new'),
    url(r'^Usuario/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^Usuario/(?P<pk>\d+)/edit/$', views.user_edit, name='user_edit'),

]