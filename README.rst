======
webmon
======

Web interface for playing back and filtering Asterisk call recordings.

Features
========

* Asterisk call log (CDR) with multiple filters
* Playback of call recordings right in your browser

Requirements
=============

* Asterisk 1.8+
* Python 2.7+

All required python packages should be installed by ``pip install -r requirements.txt``. You will need following:

* Django 1.5+
* MySQL-python
* South
* Unipath
* dj-database-url
* django-braces
* django-model-utils


Installation
============

Create MySQL database, e.g. 'asterisk'. Then create following table for asterisk CDR:

.. code-block:: sql

    CREATE TABLE `cdr` (
        `_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `clid` varchar(80) NOT NULL DEFAULT '',
        `src` varchar(30) NOT NULL DEFAULT '',
        `dst` varchar(30) NOT NULL DEFAULT '',
        `start` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `answer` timestamp NULL DEFAULT NULL,
        `end` timestamp NULL DEFAULT NULL,
        `duration` double unsigned NOT NULL DEFAULT '0',
        `billsec` double unsigned NOT NULL DEFAULT '0',
        `disposition` int(3) unsigned NOT NULL DEFAULT '0',
        `uniqueid` varchar(32) NOT NULL,
        `recordingfile` varchar(255) NOT NULL DEFAULT '',
        PRIMARY KEY (`_id`),
        KEY `start` (`start`)
    ) ENGINE=MyISAM CHARSET=utf8

Configure Asterisk to store CDR in that table. Example configuration of cdr_adaptive_odbc.conf:

.. code-block:: ini

    [webmon]
    connection=asterisk
    table=cdr

You also need to set path to recording file in Asterisk's dial plan::

    Set(CDR(recordingfile)=<path>)

Add callback to ``MixMonitor`` application to convert recordings to mp3 and ogg::

    Set(MIXMON_POST = /usr/local/scripts/convert_recording.sh ^{MIXMON_DIR}^{YEAR}/^{MONTH}/^{DAY}/^{CALLFILENAME}.^{MIXMON_FORMAT} > /dev/null 2>&1)
    MixMonitor(${MIXMON_DIR}${YEAR}/${MONTH}/${DAY}/${CALLFILENAME}.${MIXMON_FORMAT},,${MIXMON_POST})

Example of convert_recording.sh:

.. code-block:: bash

    #! /bin/bash

    FILENAME=$1
    BASENAME="${FILENAME%.*}"

    /usr/bin/lame --cbr --resample 11.025 ${FILENAME} ${BASENAME}.mp3
    /usr/bin/oggenc ${FILENAME} -o ${BASENAME}.ogg

Set environment variables::

    PYTHONPATH=/path/to/repo_root/webmon
    DJANGO_SETTINGS_MODULE=webmon.settings.production
    SECRET_KEY=<django_secret_key>
    DATABASE_URL=mysql://<user_name>:<password>@localhost:3306/<db_name>

Run ``django-admin.py syncdb``

Instructions on deploying Django project can be found here_.

.. _here: https://docs.djangoproject.com/en/1.5/howto/deployment/
