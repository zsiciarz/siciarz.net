# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import django.utils.timezone
import model_utils.fields
from django.conf import settings
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('status', model_utils.fields.StatusField(verbose_name='status', default='draft', max_length=100, no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')])),
                ('status_changed', model_utils.fields.MonitorField(verbose_name='status changed', default=django.utils.timezone.now, monitor='status')),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('subtitle', models.CharField(verbose_name='subtitle', default='', max_length=255, blank=True)),
                ('slug', models.SlugField(verbose_name='slug', unique=True, max_length=255)),
                ('summary', markitup.fields.MarkupField(verbose_name='summary', no_rendered_field=True)),
                ('content', markitup.fields.MarkupField(verbose_name='content', no_rendered_field=True)),
                ('pageviews', models.PositiveIntegerField(verbose_name='pageviews', default=0)),
                ('is_static', models.BooleanField(verbose_name='static page?', default=False)),
                ('language', models.CharField(verbose_name='language', default='pl', max_length=5, choices=[('pl', 'Polish'), ('en', 'English')])),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=127), default=list, blank=True, size=None)),
                ('header_image', models.ImageField(verbose_name='header image', upload_to='articles/%Y/%m/%d', null=True, blank=True)),
                ('_summary_rendered', models.TextField(editable=False, blank=True)),
                ('_content_rendered', models.TextField(editable=False, blank=True)),
                ('author', models.ForeignKey(verbose_name='author', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'ordering': ['-created'],
            },
        ),
    ]
