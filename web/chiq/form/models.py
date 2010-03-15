from django.db import models
from django.forms import ModelForm

class ProgrammingLanguagesAndFrameworks(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.name)


class Mentor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
       return u'%s %s' % (self.name, self.surname)


class Project(models.Model):
    name = models.TextField()
    objective = models.TextField()
    todo = models.TextField()
    prerequisites = models.TextField()
    references = models.TextField()
    score = models.TextField()
    mentors = models.ManyToManyField(Mentor)

    def __unicode__(self):
       return u'%s' % (self.name)

    class Meta:
        ordering = ('name',)



class Student(models.Model):

    # REQUIRED NOT REQUIRED BELIRLE

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField(max_length=50)
    gender = models.CharField(max_length=1)
    id_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    website = models.URLField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gpa = models.CharField(max_length=10)
    programming_languages_and_frameworks = models.ManyToManyField(ProgrammingLanguagesAndFrameworks, max_length=50)
    other_programming_languages = models.CharField(max_length=100, null=True)
    awards = models.CharField(max_length=1000, null=True)
    why_pardus = models.CharField(max_length=1000)
    projects_done = models.CharField(max_length=1000, null=True)
    where_did_you_hear = models.CharField(max_length=1000)
    suitable_date = models.CharField(max_length=50)
    prefered_projects = models.ManyToManyField(Project, max_length=200)
    commited_before = models.CharField(max_length=100)

    cv_upload = models.FileField(upload_to='attachments', null=True)


    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)

