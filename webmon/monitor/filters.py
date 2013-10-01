# -*- coding: utf-8 -*-
import django_filters
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import CallDataRecord


class CallDataRecordFilter(django_filters.FilterSet):
    start_from = django_filters.DateFilter(name='start', lookup_type='gt', label=_('From'))
    start_to = django_filters.DateFilter(name='start', lookup_type='lt', label=_('To'))
    destination = django_filters.CharFilter(lookup_type='contains', label=_('Destination'))
    disposition = django_filters.MultipleChoiceFilter(choices=CallDataRecord.DISPOSITION,
                                                      widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = CallDataRecord
        fields = ['start_from', 'start_to', 'source', 'destination', 'disposition']