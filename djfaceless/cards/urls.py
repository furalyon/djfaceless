from django.conf.urls import patterns, include, url
from django.contrib import admin
from djfaceless.cards import views

urlpatterns = patterns('',
    url(r'^$', views.BrowseView.as_view(), name='browse'),
)
