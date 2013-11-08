# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from monitor import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.CallDataRecordListView.as_view(), name='cdr_list'),
    url(r'^download/mp3/$', views.Mp3DownloadView.as_view(), name='download_mp3'),
    url(r'^download/ogg/$', views.OggDownloadView.as_view(), name='download_ogg'),
    url(r'^originate/$', views.Originate.as_view(), name='originate'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
