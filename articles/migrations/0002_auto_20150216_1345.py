# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(max_length=5, choices=[('pl', 'Polish'), ('en', 'English')], default='pl', verbose_name='language'),
            preserve_default=True,
        ),
    ]
