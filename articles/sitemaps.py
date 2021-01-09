# Copyright (c) Zbigniew Siciarz 2009-2021.

from django.contrib.sitemaps import Sitemap
from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.published.all()

    def lastmod(self, obj):
        return obj.modified
