# -*- coding: utf-8 -*-
import re
from django.db.models import Q
from tablet.tabletpc.models import TabletPC


def search(request):
    """
    Verarbeitet Tablet-Computer-Suchaufrufe von Views,
    gibt den Query-String und gefundene Sucheinträge zurück.
    """

    query_string = ''
    found_entries = None
    search_fields=('name','intro','info',)

    if ('q' in request.GET) and request.GET['q'].strip():

        query_string = request.GET['q']
        entry_query = get_query(query_string, search_fields)
        found_entries = TabletPC.objects.filter(entry_query).order_by('-id')

    return query_string, found_entries


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """ 
    Teilt den Query-String in einzelne Stichwörte, wird unnötige 
    Leerzeichen los und gruppiert zitierte Wörter zusammen.
    """

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 


def get_query(query_string, search_fields):
    """ 
    Gibt eine Abfrage/Query, dass eine Kombination von Q-Objekten ist, zurück. 
    Diese Kombination sucht Schlüsselwörter innerhalb eines Models durch die 
    Prüfung der gegebenen Suchfelder.
    """

    query = None # Abfrage, um für jeden Suchbegriff zu suchen      
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Abfrage für einen bestimmten Begriff in jedem Feld zu suchen
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
