# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2014.

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import F
from django.db.models.query import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djorm_expressions.base import SqlExpression
from djorm_expressions.models import ExpressionQuerySet
from djorm_pgarray.fields import ArrayField
from markitup.fields import MarkupField
from model_utils import Choices
from model_utils.managers import PassThroughManager
from model_utils.models import StatusModel, TimeStampedModel


class ArticleQuerySet(ExpressionQuerySet):
    def published(self):
        return self.filter(status='published')

    def only_articles(self):
        return self.filter(is_static=False)

    def only_static(self):
        return self.filter(is_static=True)

    def tagged(self, tag):
        return self.where(
            SqlExpression("tags", "@>", [tag])
        )


@python_2_unicode_compatible
class Article(StatusModel, TimeStampedModel):
    STATUS = Choices(
        ('draft', _("draft")),
        ('published', _("published")),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), blank=True, default="", max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    summary = MarkupField(_("summary"))
    content = MarkupField(_("content"))
    pageviews = models.PositiveIntegerField(default=0, verbose_name=_("pageviews"))
    is_static = models.BooleanField(default=False, verbose_name=_("static page?"))
    language = models.CharField(_("language"), max_length=5, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
    tags = ArrayField(_("tags"), dbtype="text")

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

