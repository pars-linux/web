#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of django-simple-captcha. Django-simple-captcha is
# free software that is made available under the MIT license.
# http://www.opensource.org/licenses/mit-license.php
#
# Copyright (c) 2009 Marco Bonetti.
# http://code.google.com/p/django-simple-captcha/

import random
from captcha.conf import settings

def math_challenge():
    operators = ('+','*','-',)
    operands = (random.randint(1,10),random.randint(1,10))
    operator = random.choice(operators)
    if operands[0] < operands[1] and '-' == operator:
        operands = (operands[1],operands[0])
    challenge = '%d%s%d' %(operands[0],operator,operands[1])
    return u'%s=' %(challenge), unicode(eval(challenge))

def random_char_challenge():
    chars,ret = u'abcdefghijklmnopqrstuvwxyz', u''
    for i in range(settings.CAPTCHA_LENGTH):
        ret += random.choice(chars)
    return ret.upper(),ret

def unicode_challenge():
    chars,ret = u'äàáëéèïíîöóòüúù', u''
    for i in range(settings.CAPTCHA_LENGTH):
        ret += random.choice(chars)
    return ret.upper(), ret

def word_challenge():
    fd = file(settings.CAPTCHA_WORDS_DICTIONARY,'rb')
    l = fd.readlines()
    fd.close()
    while True:
        word = random.choice(l).strip()
        if len(word) >= settings.CAPTCHA_DICTIONARY_MIN_LENGTH and len(word) <= settings.CAPTCHA_DICTIONARY_MAX_LENGTH:
            break
    return word.upper(), word.lower()

def noise_arcs(draw,image):
    size = image.size
    draw.arc([-20,-20, size[0],20], 0, 295, fill=settings.CAPTCHA_FOREGROUND_COLOR)
    draw.line([-20,20, size[0]+20,size[1]-20], fill=settings.CAPTCHA_FOREGROUND_COLOR)
    draw.line([-20,0, size[0]+20,size[1]], fill=settings.CAPTCHA_FOREGROUND_COLOR)
    return draw

def noise_dots(draw,image):
    size = image.size
    for p in range(int(size[0]*size[1]*0.1)):
        draw.point((random.randint(0, size[0]),random.randint(0, size[1])), fill=settings.CAPTCHA_FOREGROUND_COLOR )
    return draw

def post_smooth(image):
    import ImageFilter
    return image.filter(ImageFilter.SMOOTH)
