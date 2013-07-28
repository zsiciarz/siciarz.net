# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'status', 'title', 'subtitle', 'summary', 'content',
            'is_static', 'language', 'tags',
        )
