# -*- coding: utf-8 -*-
import os
import Image
from django import template

register = template.Library()
@register.filter

def thumbnail(file, size='104x104'):
    """
    Erstellt die miniaturisierte Kopie eines gegebenen Bildes und gibt den entsprechenden Link zurück.
    """

    # die Größe definieren 
    x, y = [int(x) for x in size.split('x')]

    # den Dateinamen und den Miniatur-Dateinamen definieren
    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature

    if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)

    # wenn die Größe des Bildes nicht bereits geändert is, Größe ändern
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url

