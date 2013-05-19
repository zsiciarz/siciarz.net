# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import GalleryListView, GalleryDetailsView, PhotoDetailsView

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
)
