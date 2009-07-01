#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models

class Version(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    release_notes = models.TextField()
    download_link = models.CharField(max_length=256)
