# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2010-2012.

from django.shortcuts import render


def main(request):
    return render(request, 'index.html', {
    })
