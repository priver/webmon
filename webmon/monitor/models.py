# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


class CallDataRecord(models.Model):
    """A call data record (CDR)."""
    DISPOSITION = Choices(
        (0, 'no_answer', _('no answer')),
        (1, 'null', _('null')),
        (2, 'failed', _('failed')),
        (4, 'busy', _('busy')),
        (8, 'answered', _('answered')),
        (16, 'congestion', _('congestion')),
    )

    _id = models.PositiveIntegerField(primary_key=True)
    caller_id = models.CharField(max_length=80, db_column='clid', verbose_name=_('CallerId'))
    source = models.CharField(max_length=30, db_column='src', verbose_name=_('source'))
    destination = models.CharField(max_length=30, db_column='dst', verbose_name=_('destination'))
    start = models.DateTimeField(verbose_name=_('start'))
    answer = models.DateTimeField(verbose_name=_('answer'))
    end = models.DateTimeField(verbose_name=_('end'))
    duration = models.FloatField(verbose_name=_('duration'))
    billing_seconds = models.FloatField(db_column='billsec', verbose_name=_('billing seconds'))
    disposition = models.PositiveIntegerField(choices=DISPOSITION, verbose_name=_('disposition'))
    unique_id = models.CharField(max_length=32, db_column='uniqueid', verbose_name=_('uniqueid'))
    recording_file = models.CharField(max_length=255, db_column='recordingfile',
                                      verbose_name=_('recording file'))

    class Meta:
        managed = False
        db_table = 'cdr'
        ordering = ['-start']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        raise NotImplementedError

    def duration_timedelta(self):
        return str(datetime.timedelta(seconds=int(self.duration)))

    def billing_seconds_timedelta(self):
        return str(datetime.timedelta(seconds=int(self.billing_seconds)))

    def is_answered(self):
        return self.disposition == self.DISPOSITION.answered