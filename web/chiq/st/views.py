#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.shortcuts import get_object_or_404

from chiq.flatpages.models import FlatPage
from chiq.st.wrappers import render_response
from chiq.st.models import News

def robots(request):
    return render_response(request, 'robots.txt')

def home(request):
    mainnews = News.objects.filter(is_main=True, is_published=True).order_by("date")[:1]
    news = News.objects.filter(is_main=False, is_published=True).order_by("date")[:2]
    return render_response(request, 'home.html', locals())

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    if not news.is_published and not request.user.has_perm("st.change_news"):
        return render_response(request, "404.html")
    return render_response(request, 'news/news_detail.html', locals())

def news_printable(request, slug):
    news = get_object_or_404(News, slug=slug)
    if not news.is_published and not request.user.has_perm("editor.change_contributednews"):
        return render_response(request, "404.html")
    return render_response(request, 'news/news_printable.html', locals())

def tag_detail(request, tag):
    try:
        flatpages = FlatPage.objects.filter(tags__name__exact=tag)

    except Tag.DoesNotExist:
        raise Http404
    return render_response(request, 'tag/tag_detail.html', locals())
