import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "not-defined-here"

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django_extensions",
    "debug_toolbar",
    "rosetta",
    "dj_pagination",
    "markitup",
    "reversion",
    "sorl.thumbnail",
    "crispy_forms",
    "crispy_bootstrap3",
    "articles",
    "pgallery",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "dj_pagination.middleware.PaginationMiddleware",
)

ROOT_URLCONF = "siciarz.urls"

WSGI_APPLICATION = "siciarz.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": (os.path.join(BASE_DIR, "siciarz/templates"),),
        "OPTIONS": {
            "context_processors": (
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "siciarz.context_processors.current_site",
            ),
            "debug": DEBUG,
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "siciarz",
        "USER": os.environ.get("DATABASE_USER", "siciarz"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "siciarz"),
        "HOST": "localhost",
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

TIME_ZONE = "Europe/Warsaw"

LANGUAGE_CODE = "pl"

gettext = lambda s: s

LANGUAGES = (("pl", gettext("Polish")), ("en", gettext("English")))

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, "siciarz/media")

MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "siciarz/static")

STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "siciarz/assets"),)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

INTERNAL_IPS = ("127.0.0.1",)

MARKITUP_FILTER = (
    "articles.filters.markitup_filter",
    {
        "extensions": [
            "markdown.extensions.codehilite",
            "markdown.extensions.fenced_code",
        ]
    },
)
MARKITUP_SET = "markitup/sets/markdown"

SENTRY_DSN = ""

CRISPY_TEMPLATE_PACK = "bootstrap3"

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])
