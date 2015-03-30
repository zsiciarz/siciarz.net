from django.test import TestCase

from .models import Article
from .factories import ArticleFactory


class ArticleTestCase(TestCase):
    def test_str(self):
        article = Article(title="Hello world!")
        self.assertEqual(str(article), article.title)

    def test_update_pageviews(self):
        article = ArticleFactory()
        self.assertEqual(article.pageviews, 0)
        article.update_pageviews()
        article = Article.objects.get(pk=article.pk)
        self.assertEqual(article.pageviews, 1)
