#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import datetime

from django.shortcuts import get_object_or_404

from chiq.basin.models import *
from chiq.st.wrappers import render_response

def lastyear(request):
    years = Issue.objects.all().distinct("date__year")
    year = Issue.objects.order_by("-date")[0].date.year
    issues = Issue.objects.filter(date__year=year)
    return render_response(request, "basin/liste.html", locals())

def main(request, year):
    years = Issue.objects.all().distinct("date__year")
    issues = Issue.objects.filter(date__year=year)
    return render_response(request, "basin/liste.html", locals())

def page(request, year, month, day, slug, page):
    page = get_object_or_404(Page, issue__date=datetime.date(int(year),int(month),int(day)), issue__publication__slug=slug, number=int(page))
    return render_response(request, "basin/sayfa.html", locals())
