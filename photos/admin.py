# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

"""
Administration for photos and galleries.
"""

from django.contrib import admin

import reversion

from .models import Gallery, Photo


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


class PhotoAdmin(reversion.VersionAdmin):
    """
    Administration for photos.
    """
    list_display = (
        'title', 'gallery', 'author',
    )
    list_display_links = ('title',)
    date_hierarchy = 'created'


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
