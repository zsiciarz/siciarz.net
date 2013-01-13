# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from django.views.generic import ListView, DetailView, MonthArchiveView


from .models import Article


class StaffAccessMixin(object):
    u"""
    Allow staff members to see all articles, including drafts.
    """
    def get_queryset(self):
        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.published.all()


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


class ArticleDetailsView(StaffAccessMixin, DetailView):

    def get_object(self):
        article = super(ArticleDetailsView, self).get_object()
        article.update_pageviews()
        return article
