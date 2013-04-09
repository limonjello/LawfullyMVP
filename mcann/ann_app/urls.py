from django.conf.urls import patterns, url

from ann_app import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.home),
    url(r'^aboutus', views.aboutus),
    url(r'^blog-post', views.blogpost),
    url(r'^blog', views.blog),
    url(r'^coming-soon', views.comingsoon),
    url(r'^contact', views.contact),
    url(r'^faq', views.faq),
    url(r'^features', views.features),
    url(r'^portfolio', views.portfolio),
    url(r'^pricing', views.pricing),
    url(r'^reset', views.reset),
    url(r'^signin', views.signin),
    url(r'^signup', views.signup),
    url(r'^template', views.template),
    url(r'^profile', views.profile),
)