# -*- coding: utf-8 -*-
from tablet.tabletpc.models import Brand, TabletPC, News
from django.shortcuts import render_to_response
from django.template import RequestContext
from functions import search
from django.db.models import Q


def show(request):
    """
    Gibt die Marken, die neuesten zwanzig Tablet-Computer Namen; 
    wenn verfügbar, die letzte Nachrichts-Titel, Einführungstext; 
    gesucht und gefundene Tablet-Computer für die Index-Seite zurück.
    """

    brands = Brand.objects.order_by('name')
    tablets = TabletPC.objects.order_by('-id')[:20]

    try: 
        news = News.objects.order_by('-id')[:1].get()
        news_title = news.title
        news_intro = news.intro

    except News.DoesNotExist:
        news = news_title = news_intro = None

    query_string, found_entries = search(request)

    return render_to_response(
        'index.html', {'query_string': query_string, 
                       'found_entries': found_entries,
                       'brands': brands,
                       'tablets': tablets,
                       'news_title': news_title,
                       'news_intro': news_intro},
                       context_instance=RequestContext(request))


def show_brand(request, name):
    """
    Gibt den Markennamen, die Information, das Logo, 
    die entsprechenden Nachrichten und Tablet-Computer; 
    gesucht und gefundene Tablet-Computer für die
    Marken-Seite zurück.
    """

    try:
        name = name.replace('-', ' ').title() 
        brand = Brand.objects.get(name=name)
        brand_name = brand.name
        brand_info = brand.info
        brand_logo = brand.logo
        brand_tablet = TabletPC.objects.filter(brand__name=name)
        brand_news = News.objects.filter(brand__name=name)

    except Brand.DoesNotExist:
        brand = brand_name = brand_info = None
        brand_logo = brand_tablet = brand_news = None

    query_string, found_entries = search(request)

    return render_to_response(
        'brand.html', {'name': name,
                       'brand_name': brand_name,
                       'brand_info': brand_info,
                       'brand_news': brand_news,
                       'brand_logo': brand_logo,
                       'brand_tablet': brand_tablet,
                       'query_string': query_string, 
                       'found_entries': found_entries},
                       context_instance=RequestContext(request))


def tablet_detail(request, name):
    """
    Gibt alle Felder eines bestimmten Tablet-Computers;
    gesucht und gefundene Tablet-Computer für die 
    Tablet-Seite zurück.
    """

    name = name.replace('-', ' ')

    tablet = TabletPC.objects.get(name=name)
    tablet_name = tablet.name
    tablet_intro = tablet.intro
    tablet_info = tablet.info
    tablet_os = tablet.os
    tablet_link = tablet.link
    tablet_pic = [tablet.pic1, tablet.pic2, tablet.pic3, tablet.pic4]
    tablet_brand = tablet.brand
    tablet_news = News.objects.filter(tablet__name=name)

    query_string, found_entries = search(request)

    return render_to_response(
        'tablet.html', {'query_string': query_string, 
                        'found_entries': found_entries,
                        'tabletpc': tablet,
                        'tablet_name': tablet_name,
                        'tablet_intro': tablet_intro,
                        'tablet_info': tablet_info,
                        'tablet_os': tablet_os, 
                        'tablet_pic': tablet_pic,
                        'tablet_link': tablet_link,
                        'tablet_news': tablet_news,
                        'tablet_brand': tablet_brand},
                        context_instance=RequestContext(request))


def news_detail(request, title):
    """
    Gibt alle Felder einer bestimmten Nachricht;
    gesucht und gefundene Tablet-Computer für die 
    Nachrichts-Seite zurück.
    """
    
    title = title.replace('-', ' ')

    news = News.objects.get(title=title)
    news_title = news.title
    news_intro = news.intro
    news_text = news.text
    news_date = news.date
    news_pic = [news.pic1, news.pic2]
    news_brand = Brand.objects.filter(news__title=title)
    news_tablet = TabletPC.objects.filter(news__title=title)

    query_string, found_entries = search(request)

    return render_to_response(
        'news.html', {'query_string': query_string, 
                      'found_entries': found_entries,
                      'news_title': news_title,
                      'news_intro': news_intro,
                      'news_text': news_text,
                      'news_date': news_date,
                      'news_pic': news_pic,
                      'news_brand': news_brand,
                      'news_tablet': news_tablet},
                      context_instance=RequestContext(request))


def news_all(request):
    """
    Gibt alle Nachrichteneingaben;
    gesucht und gefundene Tablet-Computer 
    für die Nachrichten-Seite zurück.
    """

    news = News.objects.all().order_by('-id')

    query_string, found_entries = search(request)

    return render_to_response(
        'newsall.html', {'query_string': query_string, 
                         'found_entries': found_entries,
                         'news': news},
                         context_instance=RequestContext(request))


def show_android(request):
    """
    Gibt alle Tablet-Computer mit Android-Betriebssystem,
    Nachrichten die Android-Betriebssystem enthalten;
    gesucht und gefundene Tablet-Computer für die 
    Android-Seite zurück.
    """

    tablets = TabletPC.objects.filter(os__icontains="android")
    
    tablet_news = News.objects.filter(
        Q(intro__icontains="android") | Q(text__icontains="android"))

    query_string, found_entries = search(request)

    return render_to_response(
        'android.html', {'query_string': query_string, 
                         'found_entries': found_entries,
                         'tablet_news': tablet_news,
                         'tablets': tablets},
                         context_instance=RequestContext(request))


