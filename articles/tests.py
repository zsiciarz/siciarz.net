from django.test import TestCase

from .factories import (ArticleFactory, DraftArticleFactory,
                        PublishedArticleFactory, StaticArticleFactory)
from .models import Article


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

    def test_only_articles_included(self):
        article = ArticleFactory()
        self.assertIn(article, Article.objects.only_articles())

    def test_only_articles_excluded(self):
        article = StaticArticleFactory()
        self.assertNotIn(article, Article.objects.only_articles())

    def test_only_static_included(self):
        article = StaticArticleFactory()
        self.assertIn(article, Article.objects.only_static())

    def test_only_static_excluded(self):
        article = ArticleFactory()
        self.assertNotIn(article, Article.objects.only_static())

    def test_tagged_included(self):
        article = ArticleFactory(tags=["test"])
        self.assertIn(article, Article.objects.tagged("test"))

    def test_tagged_excluded(self):
        article = ArticleFactory(tags=["serious"])
        self.assertNotIn(article, Article.objects.tagged("test"))

    def test_similar_articles(self):
        article1 = ArticleFactory(title="PTC", tags=["potato", "tomato", "cucumber"])
        article2 = ArticleFactory(title="PTC2", tags=["potato", "cucumber", "tomato"])
        article3 = ArticleFactory(title="TC", tags=["tomato", "cucumber"])
        article4 = ArticleFactory(title="CM", tags=["cheese", "milk"])
        similar = Article.objects.similar(article1)
        assert similar[0] == article2
        assert similar[1] == article3
