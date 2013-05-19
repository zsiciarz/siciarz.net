# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2009-2013.

from __future__ import unicode_literals

from django import forms

from djorm_pgarray.fields import ArrayFormField

from .models import Photo


class PhotoForm(forms.ModelForm):
    tags = ArrayFormField(label=_("tags"), required=False)

    class Meta:
        model = Photo
