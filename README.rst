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

All required python packages should be installed by `pip install -r requirements.txt`. You will need following:

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
        `dcontext` varchar(50) NOT NULL DEFAULT '',
        `channel` varchar(60) NOT NULL DEFAULT '',
        `dstchannel` varchar(60) NOT NULL DEFAULT '',
        `lastapp` varchar(30) NOT NULL DEFAULT '',
        `lastdata` varchar(80) NOT NULL DEFAULT '',
        `start` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `answer` timestamp NULL DEFAULT NULL,
        `end` timestamp NULL DEFAULT NULL,
        `duration` double unsigned NOT NULL DEFAULT '0',
        `billsec` double unsigned NOT NULL DEFAULT '0',
        `disposition` int(3) unsigned NOT NULL DEFAULT '0',
        `amaflags` int(3) unsigned NOT NULL DEFAULT '0',
        `accountcode` varchar(25) NOT NULL DEFAULT '',
        `uniqueid` varchar(32) NOT NULL,
        PRIMARY KEY (`_id`),
        KEY `start` (`start`)
    ) ENGINE=MyISAM CHARSET=utf8


