#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models

class Version(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    release_notes = models.TextField()
    status = models.BooleanField()

    def __unicode__(self):
        return self.name

    def get_release_notes_url(self):
        return "/release-notes/%s/" % self.slug

class Download(models.Model):
    version = models.ForeignKey(Version)
    title = models.CharField(max_length=32)
    type = models.IntegerField(choices=((0,"Kurulan"),(1,"Çalışan")))
    description = models.CharField(max_length=128)
    link = models.CharField(max_length=256)
    status = models.BooleanField()

    def __unicode__(self):
        return self.title
