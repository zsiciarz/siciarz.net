from django.contrib.auth.models import User
from django.test import TestCase

from .models import Article


class ArticleTestCase(TestCase):
    def test_str(self):
        article = Article(title="Hello world!")
        self.assertEqual(str(article), article.title)

    def test_update_pageviews(self):
        user = User.objects.create_user(username='user', password='password')
        article = Article.objects.create(title="Hello", author=user)
        self.assertEqual(article.pageviews, 0)
        article.update_pageviews()
        article = Article.objects.get(pk=article.pk)
        self.assertEqual(article.pageviews, 1)
