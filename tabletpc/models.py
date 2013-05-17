# -*- coding: utf-8 -*-
from django.db import models

class Brand(models.Model):
    """
    Ein Model der Tablet-Marke mit Name, Information und Logo.
    """

    name = models.CharField(max_length=30, unique=True)
    info = models.TextField(blank=True)
    logo = models.ImageField(blank=True, upload_to='logo')

    def __unicode__(self):
        return self.name


class TabletPC(models.Model):
    """
    Ein Model des Tablet-Computers mit Name, Einführung und 
    Informationen Textfelder, Betriebssystem, 4 Bildfelder, 
    Website-Link und entsprechende Marke.
    """

    name = models.CharField(max_length=40, unique=True)
    intro = models.TextField()
    info = models.TextField(blank=True)
    os = models.CharField(max_length=50)
    pic1 = models.ImageField(blank=True, upload_to='tabphoto')
    pic2 = models.ImageField(blank=True, upload_to='tabphoto')
    pic3 = models.ImageField(blank=True, upload_to='tabphoto')
    pic4 = models.ImageField(blank=True, upload_to='tabphoto')
    link = models.URLField(blank=True)
    brand = models.ForeignKey(Brand)

    def __unicode__(self):
        return self.name


class News(models.Model):
    """
    Ein Model einer Nachricht mit Titel, Einführung und Textfelder, 
    Datum, 2 Bilder, entsprechende Marke und Tablet-Computer.
    """
    title = models.CharField(max_length=60)
    intro = models.TextField()
    text = models.TextField()
    date = models.DateField()
    pic1 = models.ImageField(blank=True, upload_to='newsphoto')
    pic2 = models.ImageField(blank=True, upload_to='newsphoto')
    brand = models.ManyToManyField(Brand)
    tablet = models.ManyToManyField(TabletPC, blank=True, null=True)

    def __unicode__(self):
        return self.title
