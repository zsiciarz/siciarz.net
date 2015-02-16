# Copyright (c) Zbigniew Siciarz 2009-2015.

from django.contrib.sites.models import Site


def current_site(request):
    return {
        'current_site': Site.objects.get_current(),
    }
