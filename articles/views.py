# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, MonthArchiveView
from django.views.generic.edit import UpdateView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from .forms import ArticleForm
from .models import Article


class StaffAccessMixin(object):
    """
    Allow staff members to see all articles, including drafts.

    Note: 'static' pages are excluded.
    """
    def get_queryset(self):
        if self.request.user.is_staff:
            return Article.objects.only_articles()
        return Article.objects.only_articles().published()


class ArticleListView(StaffAccessMixin, ListView):
    pass


class TaggedArticleListView(ArticleListView):
    def get_queryset(self):
        queryset = super(TaggedArticleListView, self).get_queryset()
        return queryset.filter(tags__name__in=[self.kwargs['tag']])


class ArticleMonthArchiveView(StaffAccessMixin, MonthArchiveView):
    date_field = 'created'
    month_format = '%m'
    make_object_list = True


class ArticleDetailsView(DetailView):
    """
    We need to access static pages here too, so no StaffAccessMixin.
    """
    def get_queryset(self):
        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.objects.published()

    def get_object(self):
        article = super(ArticleDetailsView, self).get_object()
        article.update_pageviews()
        return article


class ArticleUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
