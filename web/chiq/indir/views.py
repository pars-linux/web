#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.shortcuts import get_object_or_404

from chiq.indir.models import Download, Version
from chiq.st.wrappers import render_response

def main(request):
    version = Version.objects.filter(status=True)[0]
    downloads = Download.objects.filter(version=version, status=True)
    return render_response(request, "indir.html", locals())

def release_notes(request, slug):
    version = get_object_or_404(Version, slug=slug, status=True)
    return render_response(request, "surum_notlari.html", locals())
