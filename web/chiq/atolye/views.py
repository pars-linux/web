#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import MySQLdb

from chiq.captcha.fields import CaptchaField

from django import forms

from chiq.atolye.models import Student, ProgrammingLanguagesAndFrameworks

CHOICES = ( (u'Yes', u'Evet'),
            (u'No', u'Hayır'))

DATES = ( (u'Cumartesi', u'Cumartesi 12:00 - 13:20'),
        (u'Pazar', u'Pazar 11:15 - 12:45'))

PROGRAMMING_LANGUAGES = ( (u'Python', u'Python'),
                          (u'C', u'C'),
                          (u'C++', u'C++'),
                          (u'Ruby', u'Ruby'),
                          (u'Java', u'Java'),
                          (u'HTML', u'HTML'),
                          (u'Qt', u'Qt'),
                          (u'Django', u'Django'),
                          (u'Javascript', u'Javascript'),
                          (u'Shellscript', u'Shellscript'),
                          (u'Rails', u'Rails'),
                          )


class AtolyeForm(forms.Form):

    name = forms.CharField(max_length=50, label="Ad", widget=forms.TextInput)
    surname = forms.CharField(max_length=50, label="Soyad", widget=forms.TextInput)
    email = forms.EmailField(label="E-posta Adresi", max_length="100", widget=forms.TextInput)
    jabber = forms.EmailField(label="Jabber Adresi", max_length="100", widget=forms.TextInput, required=False)
    website = forms.URLField(label="Web Sitesi", max_length="100" ,required=False)
    school = forms.CharField(label="Üniversite Adı", max_length=100, widget=forms.TextInput)
    department = forms.CharField(label="Bölüm", max_length=100, widget=forms.TextInput)
    programming_languages_and_frameworks = forms.MultipleChoiceField(
            PROGRAMMING_LANGUAGES,
            label="Bildiğiniz programlama dilleri ve Frameworkler",
            widget = forms.CheckboxSelectMultiple,required=False 
            )
    other_programming_languages = forms.CharField(label = "Bildiğiniz diğer programlama dilleri", max_length = 100, required=False)
    is_using_pardus = forms.ChoiceField(CHOICES, label = "Öntanımlı işletim sisteminiz Pardus mu?")
    projects_done = forms.CharField(label = "Projeleriniz", widget=forms.Textarea, max_length=200, required=False)
    using_linux_since = forms.CharField(label = "Ne zamandır Linux kullanıyorsunuz?", max_length=50, widget = forms.TextInput, required=False)
    date = forms.ChoiceField(label="Tercih ettiğiniz atölye tarihi", choices=DATES)
    comments = forms.CharField(label="Görüş ve Açıklamalar", max_length = 200, widget=forms.Textarea, required=False)
    captcha = CaptchaField(label="Doğrulama Sorusu")


def showForm(request):

    if request.method == 'POST': # If the form has been submitted...
        form = AtolyeForm(request.POST, label_suffix=' ') # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            jabber = form.cleaned_data['jabber']
            website = form.cleaned_data['website']
            school = form.cleaned_data['school']
            department = form.cleaned_data['department']
            programming_languages_and_frameworks = " ".join(form.cleaned_data['programming_languages_and_frameworks'])
            other_programming_languages = form.cleaned_data['other_programming_languages']
            is_using_pardus = form.cleaned_data['is_using_pardus']
            projects_done = form.cleaned_data['projects_done']
            using_linux_since = form.cleaned_data['using_linux_since']
            date = form.cleaned_data['date']
            comments = form.cleaned_data['comments']

            recipients = ['gokcen@pardus.org.tr']

            message = """
Ad                             : %s
Soyad                          : %s
Eposta                         : %s
Jabber                         : %s
Websitesi                      : %s
Okul                           : %s
Bolum                          : %s
Programlama Dilleri            : %s
Diger Programlama Dilleri      : %s
Pardus Kullanicisi             : %s
Projeler                       : %s
Ne zamandir Pardus kullaniyor  : %s
Tercih edilen tarihi           : %s
Gorusler                       : %s
"""

            message = message % (name, surname, email, jabber, website, school, department, programming_languages_and_frameworks, other_programming_languages, is_using_pardus, projects_done, using_linux_since, date, comments)

            from django.core.mail import send_mail
            send_mail("BİLMÖK ATÖLYE KAYIT: " + name + " " + surname, message, email, recipients)

            return HttpResponseRedirect('/atolye/ok') # Redirect after POST
    else:
        form = AtolyeForm(label_suffix=' ') # An unbound form

    return render_to_response('atolye.html', {'form': form,})


def showThanks(request):
    return render_to_response('atolye_tesekkurler.html')
