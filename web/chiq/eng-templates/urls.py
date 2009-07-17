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

    (r'%s/^robots.txt$' % root, 'chiq.st.views.robots'),

    #Tags
    (r'%s/^etiket/$', 'django.views.generic.list_detail.object_list', dict(tag_dict)),
    (r'%s/^etiket/(?P<tag>.*)/$', 'chiq.st.views.tag_detail'),

    #Webalizer
    url(r'^admin/webalizer/', include('webalizer.urls')),

    #Django
    (r'%s/^$', 'chiq.st.views.home'),
    (r'%s/^haber/$', 'chiq.st.views.news_list'),
    (r'%s/^iletisim/$', 'chiq.st.views.contact'),
    (r'%s/^indir/$', 'chiq.indir.views.main'),
    (r'%s/^surum_notlari/(?P<slug>.*)/$', 'chiq.indir.views.release_notes'),
    (r'%s/^haber/(?P<slug>.*)/yazdir/$', 'chiq.st.views.news_printable'),
    (r'%s/^haber/(?P<slug>.*)/$', 'chiq.st.views.news_detail'),
    (r'%s/^basin/', include('chiq.basin.urls')),
    (r'%s/^arama/', 'chiq.st.views.search'),
    (r'%s/^admin/upload/image/tinymce/$', 'chiq.upload.views.image_upload'),
    (r'%s/^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'%s/^admin/(.*)', admin.site.root),
    (r'%s/^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/media' % DOCUMENT_ROOT, 'show_indexes': True}),
)
