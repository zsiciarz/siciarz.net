# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField
from model_utils import Choices
from model_utils.managers import PassThroughManager
from model_utils.models import StatusModel, TimeStampedModel
from sorl.thumbnail import ImageField


class GalleryQuerySet(QuerySet):
    def published(self):
        return self.filter(status='published')


@python_2_unicode_compatible
class Gallery(StatusModel, TimeStampedModel):
    STATUS = Choices(
        ('draft', _("draft")),
        ('published', _("published")),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    description = MarkupField(_("description"))

    objects = PassThroughManager.for_queryset_class(GalleryQuerySet)()

    class Meta:
        verbose_name_plural = _("Galleries")
        ordering = ['-created']

    def __str__(self):
        """
        The string representation of a gallery is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photos:gallery_details', [], {'slug': self.slug})

    def get_teaser_photos(self):
        return self.photos.all().order_by('created')[:4]


@python_2_unicode_compatible
class Photo(TimeStampedModel):
    gallery = models.ForeignKey(Gallery, null=True, related_name='photos', verbose_name=_("gallery"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    image = ImageField(_("image"), upload_to='photos/%Y/%m/%d')

    class Meta:
        verbose_name_plural = _("Photos")
        ordering = ['-created']

    def __str__(self):
        """
        The string representation of a photo is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photos:photo_details', [], {'pk': self.pk})
