#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.conf.urls.defaults import patterns

urlpatterns = patterns('basin.views',
    (r'^$', 'lastyear'),
    (r'^(?P<year>\d{4})/$', 'main'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[a-zA-Z\d_-]+)/(?P<page>\d+)/$', 'page'),
)
