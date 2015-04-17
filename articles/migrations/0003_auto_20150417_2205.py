# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150216_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(blank=True, size=None, default=list, base_field=models.CharField(max_length=127)),
        ),
    ]
