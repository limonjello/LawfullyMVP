from django.conf.urls import patterns, url

from storage import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^read$', views.read),
    url(r'^update/(?P<ann_id>[0-9]+)$', views.update),
    url(r'^destroy/(?P<ann_id>[0-9]+)$', views.delete),
    url(r'^search$', views.search),
    url(r'^searchraw$', views.searchraw),
)