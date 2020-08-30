# Copyright (c) Zbigniew Siciarz 2009-2020.

"""
Article syndication feeds.
"""

from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _

from .models import Article


class ArticleFeed(Feed):
    """
    RSS feed with latest articles.
    """

    title = _("siciarz.net - articles")
    link = reverse_lazy("articles:article_list")
    description = _("Latest blog articles.")

    def items(self):
        """
        Returns recent articles.
        """
        return Article.objects.published().only_articles()[:5]

    def item_title(self, item):
        """
        Returns the title of a given article.
        """
        return item.title

    def item_description(self, item):
        """
        Returns the HTML content of a given article as the items description.
        """
        return "%s\n\n%s" % (item.summary, item.content)
