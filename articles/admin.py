# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

"""
Administration for articles.
"""

from django.contrib import admin

import reversion

from .models import Article


class ArticleAdmin(reversion.VersionAdmin):
    """
    Administration for articles.
    """

    list_display = (
        'author', 'title', 'status', 'pageviews', 'created', 'modified',
        'is_static',
    )
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status', 'is_static',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
