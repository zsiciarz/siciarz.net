# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from django.contrib.sites.models import Site


def current_site(request):
    return {
        'current_site': Site.objects.get_current(),
    }
