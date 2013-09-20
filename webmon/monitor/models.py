# -*- coding: utf-8 -*-
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

    AMA_FLAGS = Choices(
        (0, 'omit', _('omit')),
        (1, 'billing', _('billing')),
        (2, 'documentation', _('documentation')),
    )

    _id = models.PositiveIntegerField(primary_key=True)
    caller_id = models.CharField(max_length=80, db_column='clid', verbose_name=_('CallerId'))
    source = models.CharField(max_length=30, db_column='src', verbose_name=_('source'))
    destination = models.CharField(max_length=30, db_column='dst', verbose_name=_('destination'))
    dnid = models.CharField(max_length=30, verbose_name=_('DNID'))
    rdnis = models.CharField(max_length=30, verbose_name=_('RDNIS'))
    context = models.CharField(max_length=50, db_column='dcontext', verbose_name=_('context'))
    channel = models.CharField(max_length=60, verbose_name=_('channel'))
    destination_channel = models.CharField(max_length=60, db_column='dstchannel',
                                           verbose_name=_('destination channel'))
    last_app = models.CharField(max_length=30, db_column='lastapp', verbose_name=_('last app'))
    last_data = models.CharField(max_length=80, db_column='lastdata', verbose_name=_('last data'))
    start = models.DateTimeField(verbose_name=_('start'))
    answer = models.DateTimeField(verbose_name=_('answer'))
    end = models.DateTimeField(verbose_name=_('end'))
    duration = models.FloatField(verbose_name=_('duration'))
    billing_seconds = models.FloatField(db_column='billsec', verbose_name=_('billing seconds'))
    disposition = models.PositiveIntegerField(choices=DISPOSITION, verbose_name=_('disposition'))
    ama_flags = models.PositiveIntegerField(choices=AMA_FLAGS, db_column='amaflags',
                                            verbose_name=_('AMA flags'))
    account_code = models.CharField(max_length=25, db_column='accountcode',
                                    verbose_name=_('account code'))
    unique_id = models.CharField(max_length=32, db_column='uniqueid', verbose_name=_('uniqueid'))
    sequence = models.CharField(max_length=32, verbose_name=_('sequence'))

    class Meta:
        managed = False
        db_table = 'cdr'
        ordering = ['-start']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        raise NotImplementedError