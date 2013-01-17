# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin

from articles.sitemaps import ArticleSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^markitup/', include('markitup.urls')),

    url(
        r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {
            'articles': ArticleSitemap,
        }}
    ),
    url(r'^', include('articles.urls', namespace='articles')),
)
