# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

from .models import Article


class ArticleTestCase(TestCase):
    def test_str(self):
        article = Article(title="Hello world!")
        self.assertEqual(str(article), article.title)
