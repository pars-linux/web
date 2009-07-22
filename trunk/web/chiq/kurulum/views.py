#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.shortcuts import get_object_or_404

from chiq.st.wrappers import render_response
from chiq.kurulum.models import ScreenShot

def screenshot_detail(request, step):
    step = int(step)
    screenshot = get_object_or_404(ScreenShot, step=step)
    if ScreenShot.objects.filter(step=step-1).count():
        previous = ScreenShot.objects.get(step=step-1)
    if ScreenShot.objects.filter(step=step+1).count():
        next = ScreenShot.objects.get(step=step+1)
    return render_response(request, "kurulum/screenshot_detail.html", locals())
