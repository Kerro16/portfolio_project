from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuedby = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    cellphone = models.CharField(max_length=20)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_me/')
    projects = models.ManyToManyField(Project, related_name='about_mes', blank=True)
    experiences = models.ManyToManyField(Experience, related_name='about_mes', blank=True)
    skills = models.ManyToManyField(Skill, related_name='about_mes', blank=True)
    certifications = models.ManyToManyField(Certification, related_name='about_mes', blank=True)

    def __str__(self):
        return self.name