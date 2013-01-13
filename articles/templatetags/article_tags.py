# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from django import template

from articles.models import Article

register = template.Library()


@register.assignment_tag
def get_top_articles(count=3):
    u"""
    Returns top articles by pageview count.
    """
    return Article.published.all().order_by('-pageviews')[:count]


@register.assignment_tag
def get_related_articles(article, count=3):
    u"""
    Returns articles with similar set of tags as the given article.
    """
    return article.tags.similar_objects()[:count]


@register.assignment_tag
def get_archive_dates():
    u"""
    Returns datetime objects for all months in which articles were written.
    """
    return Article.published.dates('created', 'month', order='DESC')

