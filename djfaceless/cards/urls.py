from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('djfaceless.cards.views',
    url(r'^$', 'browse', name='browse'),
)
