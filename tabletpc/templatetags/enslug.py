# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter


def enslug(s):
    """
    Gibt eine Zeichenkette mit normalisierten türkischen Umlauten für die URL zurück.
    """
    
    s = s.lower().replace(' ', '-')
    s = s.replace(u'ş', 's').replace(u'ı', 'i').replace(u'ö', 'o').replace(u'ü', 'u').replace(u'ğ', 'g').replace(u'ç', 'c')

    return s

enslug.is_safe = True
