#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.contrib import admin

from chiq.indir.models import Version

class VersionAdmin(admin.ModelAdmin):
    list_display = ("title", "type")
    ordering = ["-title"]
    search_fields = ["title", "description"]

admin.site.register(Version, VersionAdmin)
