#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

class Issue(models.Model):
    title = models.CharField(max_length=64)
    publication = models.ForeignKey(Publication)
    date = models.DateField()

    def __unicode__(self):
        return "%s - %s" % (self.publication.title, self.date)

class Page(models.Model):
    issue = models.ForeignKey(Issue)
    number = models.IntegerField()
    image = models.ImageField(upload_to="basin/")

    def __unicode__(self):
        return "%s - %d" % (self.issue, self.number)

    def get_absolute_url(self):
        return "/basin/%s/%s/%d/" % (self.issue.date.strftime("%Y/%m/%d"), self.issue.publication.slug, self.number)
