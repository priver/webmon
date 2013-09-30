# -*- coding: utf-8 -*-
import django_filters
from django import forms

from .models import CallDataRecord


class CallDataRecordFilter(django_filters.FilterSet):
    start_from = django_filters.DateFilter(name='start', lookup_type='gt')
    start_to = django_filters.DateFilter(name='start', lookup_type='lt')
    destination = django_filters.CharFilter(lookup_type='contains')
    disposition = django_filters.MultipleChoiceFilter(choices=CallDataRecord.DISPOSITION, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = CallDataRecord
        fields = ['start_from', 'start_to', 'source', 'destination', 'disposition']