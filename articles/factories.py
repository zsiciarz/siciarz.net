import factory

from django.contrib.auth.models import User

from .models import Article


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_%d' % n)
    email = factory.Sequence(lambda n: 'user_%d@example.com' % n)

    class Meta:
        model = User


class ArticleFactory(factory.django.DjangoModelFactory):
    title = "Hello"
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Article
