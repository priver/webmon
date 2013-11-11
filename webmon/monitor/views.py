# -*- coding: utf-8 -*-
from StringIO import StringIO
from zipfile import ZipFile

import asterisk.manager
from braces.views import LoginRequiredMixin, JSONResponseMixin, CsrfExemptMixin
from django.http import HttpResponse, Http404
from django.views.generic import View
from django_filters.views import FilterView, BaseFilterView

from .filters import CallDataRecordFilter
from .models import CallDataRecord, ExternalCall


class CallDataRecordListView(LoginRequiredMixin, FilterView):
    filterset_class = CallDataRecordFilter
    context_object_name = 'call_data_records'
    template_name = 'monitor/cdr_list.html'
    paginate_by = 100

    def get_queryset(self):
        return CallDataRecord.objects.filter(context='from-internal')


class BaseDownloadView(LoginRequiredMixin, BaseFilterView):
    filterset_class = CallDataRecordFilter
    recording_ext = '.wav'
    context_object_name = 'call_data_records'
    paginate_by = 100

    def get_queryset(self):
        return CallDataRecord.objects.filter(context='from-internal')

    def get(self, request, *args, **kwargs):
        filterset = self.get_filterset(self.get_filterset_class())
        object_list = filterset.qs
        context = self.get_context_data(object_list=object_list)
        if context['call_data_records'].exists():
            f = StringIO()
            with ZipFile(f, 'w') as zipfile:
                for cdr in context['call_data_records']:
                    zipfile.write(cdr.get_media_path() + self.recording_ext,
                                  cdr.recording_file[:-4] + self.recording_ext)

            response = HttpResponse(mimetype='application/zip')
            response['Content-Disposition'] = 'attachment; filename=recordings.zip'

            f.seek(0)
            response.write(f.read())

            return response
        else:
            raise Http404


class Mp3DownloadView(BaseDownloadView):
    recording_ext = '.mp3'


class OggDownloadView(BaseDownloadView):
    recording_ext = '.ogg'


class Originate(CsrfExemptMixin, View, JSONResponseMixin):
    def post(self, request):
        try:
            login = request.POST['login']
            password = request.POST['password']
            channel = request.POST['channel']
            extension = request.POST['extension']
        except KeyError:
            return self.render_json_response({'success': False,  'message': 'Invalid parameters'})
        else:
            manager = asterisk.manager.Manager()
            try:
                manager.connect('127.0.0.1')
                manager.login(login, password)
                event = manager.originate('SIP/{0}'.format(channel), extension, 'from-internal', 1,
                                          async=True)
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
            finally:
                manager.close()
