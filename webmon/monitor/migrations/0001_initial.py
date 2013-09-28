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
            'answer': ('django.db.models.fields.DateTimeField', [], {}),
            'billing_seconds': ('django.db.models.fields.FloatField', [], {'db_column': "'billsec'"}),
            'caller_id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_column': "'clid'"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'dst'"}),
            'disposition': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'recording_file': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'recordingfile'"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'src'"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_column': "'uniqueid'"})
        }
    }

    complete_apps = ['monitor']