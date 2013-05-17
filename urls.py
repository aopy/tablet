from django.conf.urls.defaults import patterns, include, url
from tablet.tabletpc.views import show, show_brand, tablet_detail, news_detail, news_all, show_android
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tablet.views.home', name='home'),
    # url(r'^tablet/', include('tablet.foo.urls')),
    url(r'^$', show),                   
    url(r'^marka/(?P<name>[\w|\W]+)/$', show_brand),
    url(r'^model/(?P<name>[\w|\W]+)/$', tablet_detail),
    url(u'^haber/(?P<title>[\w|\W]+)/$', news_detail),
    url(r'^haberler/$', news_all),                   
    url(r'^android/$', show_android),

    url(u'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += staticfiles_urlpatterns()
