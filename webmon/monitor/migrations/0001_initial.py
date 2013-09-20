# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {
        u'monitor.calldatarecord': {
            'Meta': {'ordering': "['-start']", 'object_name': 'CallDataRecord', 'db_table': "'cdr'", 'managed': 'False'},
            '_id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'account_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'db_column': "'accountcode'"}),
            'ama_flags': ('django.db.models.fields.PositiveIntegerField', [], {'db_column': "'amaflags'"}),
            'answer': ('django.db.models.fields.DateTimeField', [], {}),
            'billing_seconds': ('django.db.models.fields.FloatField', [], {'db_column': "'billsec'"}),
            'caller_id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_column': "'clid'"}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'dcontext'"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'dst'"}),
            'destination_channel': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'dstchannel'"}),
            'disposition': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'dnid': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'last_app': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'lastapp'"}),
            'last_data': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_column': "'lastdata'"}),
            'rdnis': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'src'"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_column': "'uniqueid'"})
        }
    }

    complete_apps = ['monitor']