# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from .feeds import ArticleFeed
from .views import ArticleListView, TaggedArticleListView, ArticleDetailsView


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
        regex=r'^(?P<slug>[-\w]+)/$',
        view=ArticleDetailsView.as_view(),
        name='article_details'
    ),
)
