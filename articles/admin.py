# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

"""
Administration for articles.
"""

from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    Administration for articles.
    """

    list_display = ('author', 'title', 'status', 'pageviews', 'created', 'modified')
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
