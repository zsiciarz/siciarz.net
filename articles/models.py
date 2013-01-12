# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from markupfield.fields import MarkupField
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager


class Article(StatusModel, TimeStampedModel):
    STATUS = Choices(
        ('draft', _(u"draft")),
        ('published', _(u"published")),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"author"))
    title = models.CharField(_(u"title"), max_length=255)
    subtitle = models.CharField(_(u"subtitle"), blank=True, default="", max_length=255)
    slug = models.SlugField(_(u"slug"), max_length=255, unique=True)
    summary = MarkupField(_(u"summary"), default_markup_type='markdown')
    content = MarkupField(_(u"content"), default_markup_type='markdown')

    tags = TaggableManager()

    class Meta:
        verbose_name_plural = _(u"Articles")
        ordering = ['-created']

    def __unicode__(self):
        u"""
        The Unicode representation of an article is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('articles:article_details', [], {'slug': self.slug})

