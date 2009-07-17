#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TÜBİTAK UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="İsim", max_length=32)
    email = forms.EmailField(label="E-posta")
    company = forms.CharField(label="Şirket", max_length=32, required=False)
    text = forms.CharField(label="Sorunuz", max_length=1024, widget=forms.Textarea)

class SearchForm(forms.Form):
    term = forms.CharField(label='Anahtar kelime', required=True, widget=forms.TextInput(attrs={'size': '40',}))
