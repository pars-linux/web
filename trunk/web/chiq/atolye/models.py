#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class ProgrammingLanguagesAndFrameworks(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.name)


class Student(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    website = models.URLField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    jabber = models.EmailField(max_length=100, null=True)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    programming_languages_and_frameworks = models.ManyToManyField(ProgrammingLanguagesAndFrameworks, max_length=50)
    other_programming_languages = models.CharField(max_length=100, null=True)
    is_using_pardus = models.BooleanField(max_length=3)
    projects_done = models.CharField(max_length=200, null=True)
    using_linux_since = models.CharField(max_length=3, null=True)
    comments = models.DateField(max_length=200, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)
