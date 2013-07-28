# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from .feeds import ArticleFeed
from .views import ArticleListView, TaggedArticleListView, \
    ArticleMonthArchiveView, ArticleDetailsView, ArticleCreateView, \
    ArticleUpdateView


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=ArticleListView.as_view(),
        name='article_list'
    ),
    url(
        regex=r'^rss/$',
        view=ArticleFeed(),
        name='rss'
    ),
    url(
        regex=r'^blog/(?P<slug>[-\w]+)/$',
        view=RedirectView.as_view(url='/%(slug)s/', permanent=True),
    ),
    url(
        regex=r'^tag/(?P<tag>\w+)/$',
        view=TaggedArticleListView.as_view(),
        name='tagged_article_list'
    ),
    url(
        regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$',
        view=ArticleMonthArchiveView.as_view(),
        name='month_archive'
    ),
    url(
        regex=r'^create/$',
        view=ArticleCreateView.as_view(),
        name='article_create'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view=ArticleDetailsView.as_view(),
        name='article_details'
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/update/$',
        view=ArticleUpdateView.as_view(),
        name='article_update'
    ),
)
