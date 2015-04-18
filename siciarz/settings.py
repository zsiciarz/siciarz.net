import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'not-defined-here'

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'django_extensions',
    'debug_toolbar',
    'rosetta-grappelli',
    'rosetta',
    'compressor',
    'twitter_bootstrap',
    'pagination',
    'markitup',
    'reversion',
    'sorl.thumbnail',
    'easy_pjax',
    'raven.contrib.django.raven_compat',
    'crispy_forms',

    'articles',
    'pgallery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'siciarz.urls'

WSGI_APPLICATION = 'siciarz.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': (
            os.path.join(BASE_DIR, 'siciarz/templates'),
        ),
        'OPTIONS': {
            'context_processors': (
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.request',
                'django.core.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'siciarz.context_processors.current_site',
            ),
            'debug': DEBUG,
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'siciarz',
        'USER': os.environ.get('DATABASE_USER', 'siciarz'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'siciarz'),
        'HOST': 'localhost',
    }
}

TIME_ZONE = 'Europe/Warsaw'

LANGUAGE_CODE = 'pl'

ugettext = lambda s: s

LANGUAGES = (
    ('pl', ugettext('Polish')),
    ('en', ugettext('English')),
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'siciarz/media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'siciarz/static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'siciarz/assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

INTERNAL_IPS = ('127.0.0.1',)

GRAPPELLI_INDEX_DASHBOARD = 'siciarz.dashboard.CustomIndexDashboard'

GRAPPELLI_ADMIN_TITLE = "siciarz.net"

MARKITUP_FILTER = ('articles.filters.markitup_filter', {'extensions': ['codehilite']})
MARKITUP_SET = 'markitup/sets/markdown'

RAVEN_CONFIG = {
    'dsn': '',
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

if not DEBUG:
    COMPRESS_PRECOMPILERS = (
        ('text/less', '%s {infile} {outfile}' % os.path.join(BASE_DIR, 'node_modules/.bin/lessc')),
    )
