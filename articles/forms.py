# Copyright (c) Zbigniew Siciarz 2009-2021.

from braces.forms import UserKwargModelFormMixin
from django import forms
from slugify import slugify

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "status",
            "title",
            "subtitle",
            "header_image",
            "summary",
            "content",
            "is_static",
            "language",
            "tags",
        )


class ArticleCreateForm(UserKwargModelFormMixin, ArticleForm):
    def save(self, *args, **kwargs):
        kwargs["commit"] = False
        article = super().save(*args, **kwargs)
        article.author = self.user
        article.slug = slugify(article.title)
        article.save()
        self.save_m2m()
        return article
