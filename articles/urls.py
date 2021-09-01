# Copyright (c) Zbigniew Siciarz 2009-2021.

from django.urls import re_path
from django.views.generic.base import RedirectView

from .feeds import ArticleFeed
from .views import (
    ArticleListView,
    ArticleDashboardView,
    TaggedArticleListView,
    ArticleMonthArchiveView,
    ArticleDetailsView,
    ArticleCreateView,
    ArticleUpdateView,
)


app_name = "articles"

urlpatterns = [
    re_path(route=r"^$", view=ArticleListView.as_view(), name="article_list"),
    re_path(
        route=r"^dashboard/$",
        view=ArticleDashboardView.as_view(),
        name="article_dashboard",
    ),
    re_path(route=r"^rss/$", view=ArticleFeed(), name="rss"),
    re_path(
        route=r"^blog/(?P<slug>[-\w]+)/$",
        view=RedirectView.as_view(url="/%(slug)s/", permanent=True),
    ),
    re_path(
        route=r"^tag/(?P<tag>[\w\-\.\ ]+)/$",
        view=TaggedArticleListView.as_view(),
        name="tagged_article_list",
    ),
    re_path(
        route=r"^(?P<year>\d{4})/(?P<month>\d+)/$",
        view=ArticleMonthArchiveView.as_view(),
        name="month_archive",
    ),
    re_path(
        route=r"^create/$", view=ArticleCreateView.as_view(), name="article_create"
    ),
    re_path(
        route=r"^(?P<slug>[-\w]+)/$",
        view=ArticleDetailsView.as_view(),
        name="article_details",
    ),
    re_path(
        route=r"^(?P<slug>[-\w]+)/update/$",
        view=ArticleUpdateView.as_view(),
        name="article_update",
    ),
]
