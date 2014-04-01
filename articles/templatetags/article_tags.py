# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2014.

from __future__ import unicode_literals

from django import template

from articles.models import Article

register = template.Library()


@register.assignment_tag
def get_top_articles(count=3):
    """
    Returns top articles by pageview count.
    """
    return Article.objects.only_articles().published().order_by('-pageviews')[:count]


@register.assignment_tag
def get_related_articles(article, count=3):
    """
    Returns articles with similar set of tags as the given article.
    """
    return Article.objects.only_articles().published().similar(article)[:count]


@register.assignment_tag
def get_archive_dates():
    """
    Returns datetime objects for all months in which articles were written.
    """
    return Article.objects.only_articles().published().datetimes('created', 'month', order='DESC')
