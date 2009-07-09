#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField()
    image = models.ImageField(upload_to="urunler/")
    sum = models.TextField()
    text = models.TextField()
    is_published = models.BooleanField()

    def __unicode__(self):
        return self.name
