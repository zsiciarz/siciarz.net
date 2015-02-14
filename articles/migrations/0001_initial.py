# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
import markitup.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('subtitle', models.CharField(default='', max_length=255, verbose_name='subtitle', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='slug')),
                ('summary', markitup.fields.MarkupField(no_rendered_field=True, verbose_name='summary')),
                ('content', markitup.fields.MarkupField(no_rendered_field=True, verbose_name='content')),
                ('pageviews', models.PositiveIntegerField(default=0, verbose_name='pageviews')),
                ('is_static', models.BooleanField(default=False, verbose_name='static page?')),
                ('language', models.CharField(default=b'pl', max_length=5, verbose_name='language', choices=[(b'pl', b'Polish'), (b'en', b'English')])),
                ('tags', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('header_image', models.ImageField(upload_to='articles/%Y/%m/%d', null=True, verbose_name='header image', blank=True)),
                ('_summary_rendered', models.TextField(editable=False, blank=True)),
                ('_content_rendered', models.TextField(editable=False, blank=True)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
    ]
