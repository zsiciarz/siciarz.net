# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django import template

from articles.models import Article

register = template.Library()


@register.assignment_tag
def get_top_articles(count=3):
    u"""
    Returns top articles by pageview count.
    """
    return Article.published.all().order_by('-pageviews')[:count]

