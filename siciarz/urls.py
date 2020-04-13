# Copyright (c) Zbigniew Siciarz 2009-2016.

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.views.static import serve

from articles.sitemaps import ArticleSitemap
from pgallery.sitemaps import GallerySitemap, PhotoSitemap

admin.autodiscover()


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^rosetta/", include("rosetta.urls")),
    url(r"^markitup/", include("markitup.urls")),
    url(r"^robots\.txt", TemplateView.as_view(template_name="robots.txt")),
    url(r"^404/$", TemplateView.as_view(template_name="404.html")),
    url(r"^500/$", TemplateView.as_view(template_name="500.html")),
    url(
        r"^sitemap\.xml$",
        sitemap,
        {
            "sitemaps": {
                "articles": ArticleSitemap,
                "galleries": GallerySitemap,
                "pgallery": PhotoSitemap,
            }
        },
    ),
    url(r"^photos/", include("pgallery.urls", namespace="pgallery")),
    url(r"^", include("articles.urls", namespace="articles")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r"^__debug__/", include(debug_toolbar.urls))]
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
    ]
