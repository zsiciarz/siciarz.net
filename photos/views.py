# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, MonthArchiveView

from .models import Gallery, Photo


class StaffAccessMixin(object):
    """
    Allow staff members to see all galleries, including drafts.
    """
    def get_queryset(self):
        if self.request.user.is_staff:
            return Gallery.objects.all()
        return Gallery.objects.published()


class GalleryListView(StaffAccessMixin, ListView):
    pass


class GalleryMonthArchiveView(StaffAccessMixin, MonthArchiveView):
    date_field = 'created'
    month_format = '%m'
    make_object_list = True


class GalleryDetailsView(StaffAccessMixin, DetailView):
    pass


class PhotoDetailsView(DetailView):
    model = Photo
