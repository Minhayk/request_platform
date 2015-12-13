from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^app_request_list$', views.app_request_lists, name='app_request_list'),
    url(r'^rej_request_list$', views.rej_request_lists, name='rej_request_list'),
    url(r'^cur_request_list$', views.cur_request_lists, name='cur_request_list'),
    url(r'^request_new$', views.request_new, name='request_new'),
    url(r'^request/(?P<pk>[0-9]+)/$', views.request_detail, name='request_detail'),


]

