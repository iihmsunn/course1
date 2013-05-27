from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'BiathlonApp.views.home', name='home'),
    url(r'^tracks/$', 'BiathlonApp.views.tracks', name='tracks'),
    url(r'^athletes/$', 'BiathlonApp.views.athletes', name='athletes'),
    url(r'^event/(?P<id>\d+)/$', 'BiathlonApp.views.event', name='event'),
    url(r'^track/(?P<id>\d+)/$', 'BiathlonApp.views.track', name='track'),
    url(r'^athlete/(?P<id>\d+)/$', 'BiathlonApp.views.athlete', name='athlete'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # url(r'^Biathlon/', include('Biathlon.Biathlon.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
