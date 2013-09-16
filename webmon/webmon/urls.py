# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


#admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='monitor/cdr_list.html')),
    url(r'^login/$', TemplateView.as_view(template_name='login.html')),
    #url(r'^admin/', include(admin.site.urls)),
)
