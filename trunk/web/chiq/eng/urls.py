#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.conf.urls.defaults import *

from chiq.settings import WEB_URL, DOCUMENT_ROOT, TAG_PER_PAGE
from chiq.st.models import Tag
from django.contrib import admin

root = "/".join(WEB_URL.split("/")[3:])

tag_dict = {
            'queryset': Tag.objects.all().order_by('name'),
            'template_name': 'tag/tag_main.html',
            'paginate_by': TAG_PER_PAGE,
            'template_object_name': 'tag'
           }

admin.autodiscover()
urlpatterns = patterns('',

    (r'^%s/robots.txt$' % root, 'chiq.st.views.robots'),

    #Tags
    (r'^%s/tag/$' % root, 'django.views.generic.list_detail.object_list', dict(tag_dict)),
    (r'^%s/tag/(?P<tag>.*)/$' % root, 'chiq.st.views.tag_detail'),

    #Django
    (r'^%s/$' % root, 'chiq.st.views.home'),
    (r'^%s/news/$' % root, 'chiq.st.views.news_list'),
    (r'^%s/contact/$' % root, 'chiq.st.views.contact'),
    (r'^%s/download/$' % root, 'chiq.indir.views.main'),
    (r'^%s/release_notes/(?P<slug>.*)/$' % root, 'chiq.indir.views.release_notes'),
    (r'^%s/news/(?P<slug>.*)/print/$' % root, 'chiq.st.views.news_printable'),
    (r'^%s/news/(?P<slug>.*)/$' % root, 'chiq.st.views.news_detail'),
    (r'^%s/press/' % root, include('chiq.basin.urls')),
    (r'^%s/search/' % root, 'chiq.st.views.search'),
    (r'^%s/admin/upload/image/tinymce/$' % root, 'chiq.upload.views.image_upload'),
    (r'^%s/admin/doc/' % root, include('django.contrib.admindocs.urls')),
    (r'^%s/admin/(.*)' % root, admin.site.root),
    (r'^%s/media/(.*)$' % root, 'django.views.static.serve', {'document_root': '%s/media' % DOCUMENT_ROOT, 'show_indexes': True}),
)
