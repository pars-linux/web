#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.shortcuts import get_object_or_404

from chiq.urun.models import *
from chiq.st.wrappers import render_response

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render_response(request, "urun/urun.html", locals())

def main(request):
    products = Product.objects.all()
    return render_response(request, "urun/liste.html", locals())
