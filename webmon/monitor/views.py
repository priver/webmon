# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django_filters.views import FilterView

from .filters import CallDataRecordFilter
from .models import CallDataRecord


class CallDataRecordListView(LoginRequiredMixin, FilterView):
    model = CallDataRecord
    filterset_class = CallDataRecordFilter
    context_object_name = 'call_data_records'
    template_name = 'monitor/cdr_list.html'
    paginate_by = 50
