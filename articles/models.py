# Copyright (c) Zbigniew Siciarz 2009-2020.

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import F
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from markitup.fields import MarkupField
from model_utils import Choices
from model_utils.models import StatusModel, TimeStampedModel


class ArticleQuerySet(QuerySet):
    def drafts(self):
        return self.filter(status="draft")

    def published(self):
        return self.filter(status="published")

    def only_articles(self):
        return self.filter(is_static=False)

    def only_static(self):
        return self.filter(is_static=True)

    def tagged(self, tag):
        return self.filter(tags__contains=[tag])

    def similar(self, article):
        """
        Returns articles ordered by number of common tags with the given one.
        """
        return self.extra(
            select={
                "common_tag_count": "coalesce(array_length(array(select unnest(tags) intersect select unnest(%s)), 1), 0)"
            },
            select_params=(article.tags,),
            order_by=("-common_tag_count",),
        ).exclude(pk=article.pk)


class Article(StatusModel, TimeStampedModel):
    STATUS = Choices(("draft", _("draft")), ("published", _("published")))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        verbose_name=_("author"),
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), blank=True, default="", max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    summary = MarkupField(_("summary"))
    content = MarkupField(_("content"))
    pageviews = models.PositiveIntegerField(default=0, verbose_name=_("pageviews"))
    is_static = models.BooleanField(default=False, verbose_name=_("static page?"))
    language = models.CharField(
        _("language"),
        max_length=5,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )
    tags = ArrayField(models.CharField(max_length=127), blank=True, default=list)
    header_image = models.ImageField(
        _("header image"), blank=True, null=True, upload_to="articles/%Y/%m/%d"
    )

    objects = ArticleQuerySet.as_manager()

    class Meta:
        verbose_name_plural = _("Articles")
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article_details", kwargs={"slug": self.slug})

    def update_pageviews(self):
        """
        Atomically updates pageview counter.
        """
        Article.objects.filter(pk=self.pk).update(pageviews=F("pageviews") + 1)
