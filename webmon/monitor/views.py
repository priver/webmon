# -*- coding: utf-8 -*-
import asterisk.manager
from braces.views import LoginRequiredMixin, JSONResponseMixin, CsrfExemptMixin
from django.views.generic import View
from django_filters.views import FilterView

from .filters import CallDataRecordFilter
from .models import CallDataRecord, ExternalCall


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
            try:
                manager.connect('127.0.0.1')
                manager.login(login, password)
                event = manager.originate(channel, extension, 'from-internal', 1, async=True)
                manager.logoff()
                manager.close()
            except asterisk.manager.ManagerSocketException as (errno, reason):
                return self.render_json_response({
                    'success': False,
                    'message': 'Error connecting to the manager: {0}'.format(reason),
                })
            except asterisk.manager.ManagerAuthException as reason:
                return self.render_json_response({
                    'success': False,
                    'message': 'Error logging in to the manager: {0}'.format(reason),
                })
            except asterisk.manager.ManagerException as reason:
                return self.render_json_response({
                    'success': False,
                    'message': 'Error: {0}'.format(reason),
                })
            else:
                if event.has_header('Response') and event['Response'] == 'Success':
                    call, created = ExternalCall.objects.get_or_create(
                        channel=channel, defaults={'extension': extension})
                    if not created:
                        call.extension = extension
                        call.unique_id = ''
                        call.status = ExternalCall.STATUS.originate
                        call.save()
                    return self.render_json_response({
                        'success': True,
                        'message': event.get_header('Message', ''),
                    })
                else:
                    return self.render_json_response({
                        'success': False,
                        'message': event.get_header('Message', ''),
                    })
