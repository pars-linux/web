#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.contrib import admin

from chiq.kurulum.models import ScreenShot

class ScreenShotAdmin(admin.ModelAdmin):
    ordering = ["step"]

admin.site.register(ScreenShot, ScreenShotAdmin)
