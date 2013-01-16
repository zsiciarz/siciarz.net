# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import F
from django.db.models.query import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from markupfield.fields import MarkupField
from model_utils import Choices
from model_utils.managers import PassThroughManager
from model_utils.models import StatusModel, TimeStampedModel
from taggit.managers import TaggableManager


class ArticleQuerySet(QuerySet):
    def published(self):
        return self.filter(status='published')


@python_2_unicode_compatible
class Article(StatusModel, TimeStampedModel):
    STATUS = Choices(
        ('draft', _("draft")),
        ('published', _("published")),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), blank=True, default="", max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    summary = MarkupField(_("summary"), default_markup_type='markdown')
    content = MarkupField(_("content"), default_markup_type='markdown')
    pageviews = models.PositiveIntegerField(default=0, verbose_name=_("pageviews"))
    is_static = models.BooleanField(default=False, verbose_name=_("static page?"))

    tags = TaggableManager()
    objects = PassThroughManager.for_queryset_class(ArticleQuerySet)()

    class Meta:
        verbose_name_plural = _("Articles")
        ordering = ['-created']

    def __str__(self):
        """
        The Unicode representation of an article is its title.
        """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('articles:article_details', [], {'slug': self.slug})

    def update_pageviews(self):
        """
        Atomically updates pageview counter.
        """
        Article.objects.filter(pk=self.pk).update(pageviews=F('pageviews') + 1)

