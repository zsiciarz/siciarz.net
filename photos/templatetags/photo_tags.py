# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django import template

from photos.models import Gallery

register = template.Library()


@register.assignment_tag
def get_recent_galleries(count=3):
    """
    Returns most recent galleries.
    """
    return Gallery.objects.published().order_by('-created')[:count]
