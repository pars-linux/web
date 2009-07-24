#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of django-simple-captcha. Django-simple-captcha is
# free software that is made available under the MIT license.
# http://www.opensource.org/licenses/mit-license.php
#
# Copyright (c) 2009 Marco Bonetti.
# http://code.google.com/p/django-simple-captcha/

from django.conf.urls.defaults import *

urlpatterns = patterns('captcha.views',
    url(r'image/(?P<key>\w+)/$','captcha_image',name='captcha-image'),
)
