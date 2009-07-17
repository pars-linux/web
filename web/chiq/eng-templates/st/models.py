#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.db import models
from chiq.upload.models import Image

class Tag(models.Model):
    name = models.CharField('Etiket', max_length=32, blank=False, unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/eng/tag/%s/" % self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"

class OtherFile(models.Model):
    desc = models.TextField('Açıklama')
    file = models.FileField(upload_to='dosya/')
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return unicode(self.file)

    class Meta:
        verbose_name = "Dosya"
        verbose_name_plural = "Dosyalar"

class News(models.Model):
    title = models.CharField('Başlık', max_length=32, blank=False)
    slug = models.SlugField('SEF Başlık', help_text="Haberin bağlantısını oluşturacak başlık (haber başlığıyla aynı olmalı fakat sadece küçük harf ve - içermelidir)", unique=True)
    image = models.ForeignKey(Image, verbose_name="Açılış Görseli", blank=True, null=True, help_text="Normal haber ise görselin 310x205 boyutlarında, büyük haber ise 229x81, ana haber ise görselin 742x260 boyutlarında olmasına dikkat edin! Yeni görsel eklemek için + düğmesine tıklayın.")
    sum = models.TextField('Özet', blank=False, help_text="Açılış görseli haber özetine otomatik eklenecektir.")
    text = models.TextField('Metin', blank=False)
    date = models.DateTimeField("Tarih")
    is_main = models.BooleanField('Ana Haber', blank=True)
    is_big = models.BooleanField('Büyük Haber', blank=True)
    is_published = models.BooleanField('Yayında', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="Etiketler")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/eng/news/%s/" % self.slug

    def get_printable_url(self):
        return "/eng/news/%s/print/" % self.slug

    class Meta:
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"

class SuccessStory(models.Model):
    title = models.CharField('Başlık', max_length=32, blank=False)
    slug = models.SlugField('SEF Başlık', help_text="Makalenin bağlantısını oluşturacak başlık (makale başlığıyla aynı olmalı fakat sadece küçük harf ve - içermelidir)", unique=True)
    sum = models.TextField('Özet', blank=False)
    text = models.TextField('Metin', blank=False)
    date = models.DateTimeField("Tarih")
    is_main = models.BooleanField('Ana Sayfada', blank=True)
    is_published = models.BooleanField('Yayında', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="Etiketler")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/eng/success-stories/%s/" % self.slug

    def get_printable_url(self):
        return "/eng/success-stories/%s/print/" % self.slug

    class Meta:
        verbose_name = "Başarı Öyküsü"
        verbose_name_plural = "Başarı Öyküleri"
