# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('articles.urls', namespace='articles')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^rosetta/', include('rosetta.urls'))
)
