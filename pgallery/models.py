# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from PIL import Image, ExifTags

from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from djorm_hstore.fields import DictionaryField
from djorm_hstore.models import HStoreManager
from djorm_pgarray.fields import ArrayField
from djorm_expressions.base import SqlExpression
from markitup.fields import MarkupField
from model_utils import Choices
from model_utils.managers import PassThroughManager
from model_utils.models import StatusModel, TimeStampedModel
from sorl.thumbnail import ImageField


def sanitize_exif_value(key, value):
    if isinstance(value, six.string_types):
        return value.replace('\x00', '').strip()
    return str(value)


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
    shot_date = models.DateField(_("shot date"), null=True, blank=True)

    objects = PassThroughManager.for_queryset_class(GalleryQuerySet)()

    class Meta:
        verbose_name_plural = _("Galleries")
        ordering = ['-shot_date']

    def __str__(self):
        """
        The string representation of a gallery is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('pgallery:gallery_details', [], {'slug': self.slug})

    def get_teaser_photos(self):
        return self.photos.all()[:4]


class PhotoManager(HStoreManager):
    def tagged(self, tag):
        return self.where(
            SqlExpression("tags", "@>", [tag])
        ).order_by('-gallery__shot_date')


@python_2_unicode_compatible
class Photo(TimeStampedModel):
    gallery = models.ForeignKey(Gallery, null=True, related_name='photos', verbose_name=_("gallery"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    image = ImageField(_("image"), upload_to='photos/%Y/%m/%d')
    tags = ArrayField(dbtype="text")
    exif = DictionaryField(editable=False, default='', db_index=True)

    objects = PhotoManager()

    class Meta:
        verbose_name_plural = _("Photos")
        ordering = ['created']

    def __str__(self):
        """
        The string representation of a photo is its title.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Updates EXIF data before saving.
        """
        # you really should be doing this in a background task
        img = Image.open(self.image.file)
        raw_exif = img._getexif()
        self.exif = {ExifTags.TAGS[k]: sanitize_exif_value(k, v) for k, v in raw_exif.items() if k in ExifTags.TAGS}
        super(Photo, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('pgallery:photo_details', [], {'pk': self.pk})

    def get_next_photo(self):
        """
        Returns next photo from the same gallery (in chronological order).

        Wraps around from last photo in the gallery to the first one.
        """
        try:
            next_photo = Photo.objects.filter(
                gallery=self.gallery,
                created__gt=self.created,
            )[0]
        except IndexError:
            next_photo = Photo.objects.filter(gallery=self.gallery)[0]
        return next_photo
