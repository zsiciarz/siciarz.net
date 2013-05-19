# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

"""
Administration for photos and galleries.
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

import reversion
from sorl.thumbnail.admin import AdminImageMixin

from .forms import PhotoForm
from .models import Gallery, Photo


class PhotoInline(AdminImageMixin, admin.TabularInline):
    """
    Administration for photos.
    """
    model = Photo
    form = PhotoForm
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

    def save_model(self, request, obj, form, change):
        """
        Set currently authenticated user as the author of the gallery.
        """
        obj.author = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        """
        For each photo set it's author to currently authenticated user.
        """
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Photo):
                instance.author = request.user
            instance.save()


admin.site.register(Gallery, GalleryAdmin)
