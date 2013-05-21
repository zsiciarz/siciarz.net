# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from articles.sitemaps import ArticleSitemap
from photos.sitemaps import GallerySitemap, PhotoSitemap

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^markitup/', include('markitup.urls')),
    url(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt')),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),

    url(
        r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {
            'articles': ArticleSitemap,
            'galleries': GallerySitemap,
            'photos': PhotoSitemap,
        }}
    ),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^', include('articles.urls', namespace='articles')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    )
