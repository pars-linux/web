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

class Issue(models.Model):
    publication = models.ForeignKey(Publication)
    date = models.DateField()

class Page(models.Model):
    issue = models.ForeignKey(Issue)
    number = models.IntegerField()
    image = models.ImageField(upload_to="basin/")

    def get_absolute_url(self):
        return "/basin/%s/%s/%d/" % (self.issue.date, self.issue.publication.slug, self.number)
