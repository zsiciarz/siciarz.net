# Copyright (c) Zbigniew Siciarz 2009-2021.

from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from articles.sitemaps import ArticleSitemap
from pgallery.sitemaps import GallerySitemap, PhotoSitemap

admin.autodiscover()


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^rosetta/", include("rosetta.urls")),
    re_path(r"^markitup/", include("markitup.urls")),
    re_path(r"^robots\.txt", TemplateView.as_view(template_name="robots.txt")),
    re_path(r"^404/$", TemplateView.as_view(template_name="404.html")),
    re_path(r"^500/$", TemplateView.as_view(template_name="500.html")),
    re_path(
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
    re_path(r"^photos/", include("pgallery.urls", namespace="pgallery")),
    re_path(r"^", include("articles.urls", namespace="articles")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
    ]
