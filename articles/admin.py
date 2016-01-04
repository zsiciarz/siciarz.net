# Copyright (c) Zbigniew Siciarz 2009-2016.

"""
Administration for articles.
"""

from django.contrib import admin
from django.shortcuts import redirect

from reversion.admin import VersionAdmin
from reversion.models import Revision

from .models import Article


class RevisionAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'date_created')
    search_fields = ('=user__username', '=user__email')
    date_hierarchy = ('date_created')

    def change_view(self, request, obj=None):
        self.message_user(request, 'You cannot change history.')
        return redirect('admin:reversion_revision_changelist')

admin.site.register(Revision, RevisionAdmin)


class ArticleAdmin(VersionAdmin):
    """
    Administration for articles.
    """

    list_display = (
        'author', 'title', 'status', 'pageviews', 'created', 'modified',
        'is_static',
    )
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status', 'is_static',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        """
        Set currently authenticated user as the author of the article.
        """
        obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
