from django.test import TestCase

from .models import Article
from .factories import ArticleFactory, DraftArticleFactory, PublishedArticleFactory


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

    def test_drafts_included(self):
        article = DraftArticleFactory()
        self.assertIn(article, Article.objects.drafts())

    def test_drafts_excluded(self):
        article = PublishedArticleFactory()
        self.assertNotIn(article, Article.objects.drafts())

    def test_published_included(self):
        article = PublishedArticleFactory()
        self.assertIn(article, Article.objects.published())

    def test_published_excluded(self):
        article = DraftArticleFactory()
        self.assertNotIn(article, Article.objects.published())
