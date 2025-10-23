import factory
from django.contrib.auth.models import User

from .models import Article


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.Sequence(lambda n: f"user_{n}@example.com")

    class Meta:
        model = User


class ArticleFactory(factory.django.DjangoModelFactory):
    title = "Hello"
    slug = factory.Sequence(lambda n: f"title_{n}")
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Article


class DraftArticleFactory(ArticleFactory):
    status = "draft"


class PublishedArticleFactory(ArticleFactory):
    status = "published"


class StaticArticleFactory(ArticleFactory):
    is_static = True
