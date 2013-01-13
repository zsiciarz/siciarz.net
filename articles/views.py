# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.views.generic import ListView, DetailView, MonthArchiveView


from .models import Article


class ArticleListView(ListView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        return Article.published.all()


class TaggedArticleListView(ArticleListView):
    def get_queryset(self):
        queryset = super(TaggedArticleListView, self).get_queryset()
        return queryset.filter(tags__name__in=[self.kwargs['tag']])


class ArticleMonthArchiveView(MonthArchiveView):
    date_field = 'created'
    month_format = '%m'
    make_object_list = True

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        return Article.published.all()


class ArticleDetailsView(DetailView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        return Article.published.all()

    def get_object(self):
        article = super(ArticleDetailsView, self).get_object()
        article.update_pageviews()
        return article
