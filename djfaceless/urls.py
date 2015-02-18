from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djfaceless.views.home', name='home'),
    url(r'^cards/', include('djfaceless.cards.urls', namespace='cards')),

    url(r'^admin/', include(admin.site.urls)),
)
