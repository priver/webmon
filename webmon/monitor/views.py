# -*- coding: utf-8 -*-
from django.views.generic import ListView

from .models import CallDataRecord


class CallDataRecordListView(ListView):
    model = CallDataRecord
    context_object_name = 'call_data_records'
    template_name = 'monitor/cdr_list.html'

