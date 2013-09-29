# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from monitor import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.CallDataRecordListView.as_view()),
    url(r'^login/$', TemplateView.as_view(template_name='login.html')),
    url(r'^admin/', include(admin.site.urls)),
)
