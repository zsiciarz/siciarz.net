# Copyright (c) Zbigniew Siciarz 2009-2021.

from articles.models import Article
from django import template

register = template.Library()


@register.simple_tag
def get_top_articles(count=3):
    """
    Returns top articles by pageview count.
    """
    return Article.objects.only_articles().published().order_by("-pageviews")[:count]


@register.simple_tag
def get_related_articles(article, count=3):
    """
    Returns articles with similar set of tags as the given article.
    """
    queryset = (
        Article.objects.only_articles()
        .published()
        .similar(article)
        .only("slug", "title")
    )
    return [obj for obj in queryset if obj.common_tag_count > 0][:count]


@register.simple_tag
def get_archive_dates():
    """
    Returns datetime objects for all months in which articles were written.
    """
    return (
        Article.objects.only_articles()
        .published()
        .datetimes("created", "month", order="DESC")
    )
