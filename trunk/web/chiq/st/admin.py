#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.contrib import admin

from chiq.st.models import News, Tag, OtherFile

class StSimpleAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    ordering = ['-name']
    search_fields = ['name']

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'desc')
    ordering = ['-id']
    search_fields = ['file', 'desc']

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_main', 'is_big', 'date')
    list_filter = ('date',)
    ordering = ('date',)
    search_fields = ('title', 'text', 'sum', 'tag__name')
    prepopulated_fields = {'slug': ("title",)}

    fieldsets = (
            ('Genel', {'fields': ('title', 'image', 'sum', 'text', 'tags', 'date', 'is_main', 'is_big', 'is_published')}),
            ('Diğer', {'fields': ('slug',), 'classes': 'collapse'}),
            )

    class Media:
        js = ("js/tinymce/tiny_mce.js", "js/tinymce/textareas.js", "js/jquery-1.2.6.min.js", "js/adminimages.js", "js/jquery.autocomplete.js", "js/taghelper.js")
        css = {
            "all": ("css/autocomplete.css",),
        }

admin.site.register(Tag, StSimpleAdmin)
admin.site.register(OtherFile, FileAdmin)
admin.site.register(News, NewsAdmin)
