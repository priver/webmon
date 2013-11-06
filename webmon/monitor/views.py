# -*- coding: utf-8 -*-
import asterisk.manager
from braces.views import LoginRequiredMixin, JSONResponseMixin, CsrfExemptMixin
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


class Originate(CsrfExemptMixin, View, JSONResponseMixin):
    def post(self, request):
        try:
            login = request.POST['login']
            password = request.POST['password']
            channel = 'SIP/{0}'.format(request.POST['channel'])
            extension = request.POST['extension']
        except KeyError:
            return self.render_json_response({'success': False,  'message': 'Invalid parameters'})
        else:
            manager = asterisk.manager.Manager()
            manager.connect('127.0.0.1')
            manager.login(login, password)
            event = manager.originate(channel, extension, 'from-internal', 1, async=True)
            manager.logoff()
            manager.close()
            return self.render_json_response({
                'success': event.has_header('Response') and event['Response'] == 'Success',
                'message': event.get_header('Message', '')
            })
