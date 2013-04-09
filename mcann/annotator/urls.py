from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.conf.urls import patterns, include, url
from ann_app import *
from storage import *

import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'annotator.views.home', name='home'),
    # url(r'^annotator/', include('annotator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ann/', include('ann_app.urls')),
    url(r'^storage/', include('storage.urls')),
    #url(r'^login/$', 'ann_app.views.do_login', {'template_name': 'signin.html'}, name='login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'signin.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': settings.SUB_URL+'/ann/'}, name='logout'),
    url(r'^profile/$', 'ann_app.views.profile'),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration_email.backends.default.urls')),
    #url(r'', 'ann_app.views.index'),
)
#^admin/
#^ann/
#^login/$ [name='login']
#^logout/$ [name='logout']
#^activate/complete/$ [name='registration_activation_complete']
#^activate/(?P<activation_key>\w+)/$ [name='registration_activate']
#^register/$ [name='registration_register']
#^register/complete/$ [name='registration_complete']
#^register/closed/$ [name='registration_disallowed']
#^login/$ [name='auth_login']
#^logout/$ [name='auth_logout']
#^password/change/$ [name='auth_password_change']
#^password/change/done/$ [name='auth_password_change_done']
#^password/reset/$ [name='auth_password_reset']
#^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$ [name='auth_password_reset_confirm']
#^password/reset/complete/$ [name='auth_password_reset_complete']
#^password/reset/done/$ [name='auth_password_reset_done']

#^admin/
#^ann/
#^storage/
#^login/$ [name='login']
#^logout/$ [name='logout']
#^profile/$
#^accounts/ ^activate/complete/$ [name='registration_activation_complete']
#^accounts/ ^activate/(?P<activation_key>\w+)/$ [name='registration_activate']
#^accounts/ ^register/$ [name='registration_register']
#^accounts/ ^register/complete/$ [name='registration_complete']
#^accounts/ ^register/closed/$ [name='registration_disallowed']
#^accounts/ ^login/$ [name='auth_login']
#^accounts/ ^logout/$ [name='auth_logout']
#^accounts/ ^password/change/$ [name='auth_password_change']
#^accounts/ ^password/change/done/$ [name='auth_password_change_done']
#^accounts/ ^password/reset/$ [name='auth_password_reset']
#^accounts/ ^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$ [name='auth_password_reset_confirm']
#^accounts/ ^password/reset/complete/$ [name='auth_password_reset_complete']
#^accounts/ ^password/reset/done/$ [name='auth_password_reset_done']