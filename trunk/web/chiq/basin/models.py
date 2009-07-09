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

class Bulletin(models.Model):
    title = models.CharField('Başlık', max_length=128)
    slug = models.SlugField('SEF Başlık', help_text="Makalenin bağlantısını oluşturacak başlık (makale başlığıyla aynı olmalı fakat sadece küçük harf ve - içermelidir)", unique=True)
    text = models.TextField('Metin')
    date = models.DateTimeField("Tarih")
    is_published = models.BooleanField('Yayında', blank=True, default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/basin/bulten/%s/" % self.slug

    def get_printable_url(self):
        return "/basin/bulten/%s/yazdir/" % self.slug

    class Meta:
        verbose_name = "Basın Bülteni"
        verbose_name_plural = "Basın Bültenleri"
