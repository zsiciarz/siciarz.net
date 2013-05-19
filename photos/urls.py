# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import GalleryListView, GalleryMonthArchiveView, \
    GalleryDetailsView, PhotoDetailsView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=GalleryListView.as_view(),
        name='gallery_list'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=GalleryDetailsView.as_view(),
        name='gallery_details'
    ),
    url(
        regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        view=GalleryMonthArchiveView.as_view(),
        name='month_archive'
    ),
)
