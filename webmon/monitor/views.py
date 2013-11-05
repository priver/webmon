# -*- coding: utf-8 -*-
import asterisk.manager
from braces.views import LoginRequiredMixin, JSONResponseMixin
from django.views.generic import View
from django_filters.views import FilterView

from .filters import CallDataRecordFilter
from .models import CallDataRecord


class CallDataRecordListView(LoginRequiredMixin, FilterView):
    filterset_class = CallDataRecordFilter
    context_object_name = 'call_data_records'
    template_name = 'monitor/cdr_list.html'
    paginate_by = 50

    def get_queryset(self):
        return CallDataRecord.objects.filter(context='from-internal')


class Originate(View, JSONResponseMixin):
    def post(self, request):
        try:
            login = request.POST['login']
            password = request.POST['password']
            channel = 'SIP/{0}'.format(request.POST['channel'])
            extension = request.POST['extension']
        except KeyError:
            return self.render_json_response({'success': False,  'error': 'Invalid parameters'})
        else:
            manager = asterisk.manager.Manager()
            manager.connect('127.0.0.1')
            manager.login(login, password)
            response = manager.originate(channel, extension, 'from-internal', 1, async=True)
            manager.logoff()
            manager.close()
            return self.render_json_response({'success': True, 'response': response})
