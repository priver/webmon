# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExternalCall'
        db.create_table(u'monitor_externalcall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('extension', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'monitor', ['ExternalCall'])

    def backwards(self, orm):
        # Deleting model 'ExternalCall'
        db.delete_table(u'monitor_externalcall')

    models = {
        u'monitor.calldatarecord': {
            'Meta': {'ordering': "['-start']", 'object_name': 'CallDataRecord', 'db_table': "'cdr'", 'managed': 'False'}  ,
            '_id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'answer': ('django.db.models.fields.DateTimeField', [], {}),
            'billing_seconds': ('django.db.models.fields.FloatField', [], {'db_column': "'billsec'"}),
            'caller_id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_column': "'clid'"}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'dcontext'"}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'dst'"}),
            'disposition': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'recording_file': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'recordingfi  le'"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'src'"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_column': "'uniqueid'"})
        },
        u'monitor.externalcall': {
            'Meta': {'object_name': 'ExternalCall'},
            'channel': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }
