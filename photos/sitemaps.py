# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.contrib.sitemaps import Sitemap
from .models import Gallery


class GallerySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Gallery.published.all()

    def lastmod(self, obj):
        return obj.modified
