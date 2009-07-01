#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from chiq.indir.models import Version
from chiq.st.wrappers import render_response

def main(request):
    versions = Version.objects.all()
    return render_response(request, "indir.html", locals())
