#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import logging
import re
import sys
import time

import asterisk.manager
import MySQLdb
import MySQLdb.cursors


DB_TABLE = 'monitor_externalcall'
CHANNEL_EXP = re.compile(r'^SIP/(\d{3})-')


def get_db_connection(host, user, password, db_name):
    try:
        connection = MySQLdb.connect(
            host=host, user=user, passwd=password, db=db_name,
            charset='utf8', use_unicode=True,
            cursorclass=MySQLdb.cursors.DictCursor)
    except MySQLdb.Error as e:
        logging.error('Cannot connect to database: {0}'.format(e))
        return None
    else:
        return connection


def select(cursor, channel):
    try:
        num_rows = cursor.execute(
            "SELECT * from `monitor_externalcall` WHERE `channel`='{0}'".format(channel))
        if num_rows:
            row = cursor.fetchone()
        else:
            row = None
    except MySQLdb.Error as e:
        logging.error('Database error: {0}'.format(e))
        return None
    else:
        return row


def update(cursor, channel, status, unique_id):
    try:
        cursor.execute("UPDATE `monitor_externalcall` SET `status`='{0}', `unique_id`='{1}' "
                       "WHERE `channel`='{2}'".format(status, unique_id, channel))
    except MySQLdb.Error as e:
        logging.error('Database error: {0}'.format(e))


def handle_bridge(event, manager):
    unique_id = event.get_header('Uniqueid1', '')
    channel = event.get_header('Channel1', '')
    extension = event.get_header('CallerID2', '')
    logging.debug('Received "Bridge": UniqueID: {0}, Channel: {1}, CallerID: {2}'.format(
        unique_id, channel, extension))
    try:
        channel = CHANNEL_EXP.match(channel).group(1)
    except AttributeError:
        pass
    else:
        connection = get_db_connection(*manager.db)
        with connection:
            connection.autocommit(True)
            cursor = connection.cursor()
            row = select(cursor, channel)
            if row is not None and row['status'] == 0 and row['extension'] == extension:
                update(cursor, channel, 1, unique_id)
        cursor.close()


def handle_hangup(event, manager):
    unique_id = event.get_header('Uniqueid', '')
    channel = event.get_header('Channel', '')
    logging.debug('Received "Hangup": UniqueID: {0}, Channel: {1}'.format(unique_id, channel))
    try:
        channel = CHANNEL_EXP.match(channel).group(1)
    except AttributeError:
        pass
    else:
        connection = get_db_connection(*manager.db)
        with connection:
            connection.autocommit(True)
            cursor = connection.cursor()
            row = select(cursor, channel)
            if row is not None:
                update(cursor, channel, 2, '')
        cursor.close()


def handle_shutdown(event, manager):
    logging.warning('Received shutdown event: {0}'.format(event))
    manager.close()


def main(args):
    log_level = getattr(logging, args.log.upper(), None)
    if isinstance(log_level, int):
        logging.basicConfig(level=log_level)
    else:
        logging.warning('Invalid log level: {0}'.format(args.log))

    manager = asterisk.manager.Manager()
    try:
        manager.connect(args.ami_host)
        manager.login(args.ami_user, args.ami_password)
    except asterisk.manager.ManagerSocketException as (errno, reason):
        logging.error('Error connecting to the manager: {0}'.format(reason))
        sys.exit(1)
    except asterisk.manager.ManagerAuthException as reason:
        logging.error('Error logging in to the manager: {0}'.format(reason))
        sys.exit(1)
    except asterisk.manager.ManagerException as reason:
        logging.error('Error: {0}'.format(reason))
        sys.exit(1)
    else:
        logging.info('Connected to Asterisk manager')
        manager.db = (args.mysql_host, args.mysql_user, args.mysql_password, args.mysql_db)
        manager.register_event('Bridge', handle_bridge)
        manager.register_event('Hangup', handle_hangup)
        manager.register_event('Shutdown', handle_shutdown)
        try:
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            logging.info('Terminated by user')
            manager.close()
    finally:
        manager.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ami-host', default='localhost', help='AMI hostname')
    parser.add_argument('--ami-user', default='admin', help='AMI user')
    parser.add_argument('--ami-password', required=True, help='AMI password')
    parser.add_argument('--mysql-host', default='localhost', help='MySQL hostname')
    parser.add_argument('--mysql-user', default='asterisk', help='MySQL user')
    parser.add_argument('--mysql-password', required=True, help='MySQL password')
    parser.add_argument('--mysql-db', default='asterisk', help='MySQL database name')
    parser.add_argument('--log', default='info', help='Log level (debug, info, warning, error)')
    main(parser.parse_args())