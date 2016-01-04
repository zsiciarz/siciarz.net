# Copyright (c) Zbigniew Siciarz 2009-2016.


def current_site(request):
    protocol = 'https' if request.is_secure() else 'http'
    return {
        'current_site': '{}://siciarz.net'.format(protocol),
    }
