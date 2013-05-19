# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

"""
Administration for photos and galleries.
"""

from django.contrib import admin

import reversion
from sorl.thumbnail.admin import AdminImageMixin

from .models import Gallery, Photo


class PhotoInline(AdminImageMixin, admin.TabularInline):
    """
    Administration for photos.
    """
    model = Photo
    ordering = ['created']


class GalleryAdmin(reversion.VersionAdmin):
    """
    Administration for galleries.
    """
    list_display = (
        'author', 'title', 'status', 'description', 'created', 'modified',
    )
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]


admin.site.register(Gallery, GalleryAdmin)
