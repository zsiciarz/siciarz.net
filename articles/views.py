# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        return Article.published.all()


class ArticleDetailsView(DetailView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        return Article.published.all()
