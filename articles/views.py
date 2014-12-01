# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2014.

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, MonthArchiveView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin, \
    UserFormKwargsMixin

from .forms import ArticleForm, ArticleCreateForm
from .models import Article

from pgallery.models import Gallery


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
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['latest_gallery'] = Gallery.objects.first()
        return context


class ArticleDashboardView(LoginRequiredMixin, StaffuserRequiredMixin, StaffAccessMixin, ListView):
    template_name = "articles/article_dashboard.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDashboardView, self).get_context_data(*args, **kwargs)
        context['drafts'] = Article.objects.only_articles().drafts()
        context['published'] = Article.objects.only_articles().published()
        return context


class TaggedArticleListView(StaffAccessMixin, ListView):
    def get_queryset(self):
        queryset = super(TaggedArticleListView, self).get_queryset()
        return queryset.tagged(self.kwargs['tag'])


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

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailsView, self).get_context_data(*args, **kwargs)
        try:
            context['next_article'] = self.object.get_next_by_created(status='published')
        except Article.DoesNotExist:
            context['next_article'] = None
        try:
            context['previous_article'] = self.object.get_previous_by_created(status='published')
        except Article.DoesNotExist:
            context['previous_article'] = None
        return context


class ArticleCreateView(LoginRequiredMixin, StaffuserRequiredMixin, UserFormKwargsMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm

    def get_success_url(self):
        if 'continue' in self.request.POST:
            return reverse('articles:article_update', kwargs={'slug': self.object.slug})
        else:
            return self.object.get_absolute_url()


class ArticleUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        if 'continue' in self.request.POST:
            return self.request.get_full_path()
        else:
            return self.object.get_absolute_url()
