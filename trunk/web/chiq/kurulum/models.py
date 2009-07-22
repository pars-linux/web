#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models

class ScreenShot(models.Model):
    step = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to="upload/image/")

    def __unicode__(self):
        return "%s - %s" % (self.id, self.title)
