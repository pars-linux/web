#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.contrib import admin

from chiq.basin.models import *

class BulletinAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinymce/tiny_mce.js", "js/tinymce/textareas.js")

admin.site.register(Publication, admin.ModelAdmin)
admin.site.register(Issue, admin.ModelAdmin)
admin.site.register(Page, admin.ModelAdmin)
admin.site.register(Bulletin, BulletinAdmin)
