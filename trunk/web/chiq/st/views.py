#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.db.models import Q

from chiq.flatpages.models import FlatPage
from chiq.st.wrappers import render_response
from chiq.st.models import News, SuccessStory
from chiq.st.forms import ContactForm, SearchForm

def robots(request):
    return render_response(request, 'robots.txt')

def home(request):
    if "pardus.org.tr" not in request.META.get("HTTP_REFERER", ""):
        if "tr" not in request.META.get("HTTP_ACCEPT_LANGUAGE", "en"):
            return HttpResponseRedirect("http://www.pardus.org.tr/eng/")

    mainnews = News.objects.filter(is_main=True, is_published=True).order_by("-date")[:1]
    stories = SuccessStory.objects.filter(is_main=True, is_published=True).order_by("-date")[:1]
    news = News.objects.filter(is_main=False, is_published=True, is_big=False).order_by("-date")[:2]
    bignews = News.objects.filter(is_big=True, is_published=True).order_by("-date")[:1]
    return render_response(request, 'home.html', locals())

def story_list(request):
    stories = SuccessStory.objects.filter(is_published=True).order_by("date")
    return render_response(request, 'successstory/successstory_list.html', locals())

def news_list(request):
    news = News.objects.filter(is_published=True, is_main=False).order_by("-date")
    return render_response(request, 'news/news_list.html', locals())

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

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST.copy())
        if form.is_valid():
            send_mail("Pardus.org.tr bilgi formu", form.cleaned_data["text"], "%s <%s>" % (form.cleaned_data["name"],form.cleaned_data["email"]), ["bilgi@pardus.org.tr"], fail_silently=True)
            mail_sent = True
            return render_response(request, "iletisim.html", locals())
    else:
        form = ContactForm()
    return render_response(request, "iletisim.html", locals())

def search(request):
    searched = False
    if request.method == 'POST':
        form = SearchForm(request.POST.copy())
        if form.is_valid():
            term = form.cleaned_data['term']
            flatpage_list = FlatPage.objects.filter(Q(title__icontains=term)|Q(is_active=True)|Q(text__icontains=term)).order_by('-update')[:50]
            news_list = News.objects.filter(Q(title__icontains=term)|Q(is_published=True)|Q(text__icontains=term)).order_by('-date')[:50]
            searched = True
    else:
        form = SearchForm()
    return render_response(request, "arama.html", locals())
