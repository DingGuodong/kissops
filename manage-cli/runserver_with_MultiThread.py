#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:runserver_with_MultiThread.py
User:               Guodong
Create Date:        2017/3/17
Create Time:        13:47
 """
import os
import sys
import threading
from collections import Iterable

admin_url = 'http://127.0.0.1:8000/admin/'
app_url = 'http://127.0.0.1:8000/admin/itoms/app/'


def is_port_open(host, port):
    """
    :param host: str
    :param port:  int
    :return:  boolean
    """

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(socket.AF_INET)
        return True
    except socket.error:
        return False
    finally:
        s.close()


def runserver():
    if not is_local_mysql_port_running():
        bring_up_mysql_service()
        # TODO(Guodong Ding) If we do NOT allow mysql run, the main Thread won't exit,
        # we hope it will exit when sub-Thread run into something wrong

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(BASE_DIR)
    try:
        print "Admin --> %s" % admin_url
        print "App   --> %s" % app_url
        # TODO(Guodong Ding) python non-blocking execute system command
        os.system("python manage.py runserver")  # blocking
    except OSError as e:
        print e.message
        sys.exit(1)


def openWebBrowser():
    import webbrowser
    import time
    while True:
        if is_port_open('127.0.0.1', 8000):
            webbrowser.open(app_url)
            webbrowser.open(admin_url)
            break
        else:
            time.sleep(0.2)


def is_local_mysql_port_running():
    if is_port_open('127.0.0.1', 3306):
        return True
    else:
        return False


def is_local_mysql_service_running():
    MYSQL_WIN32_SERVICE_NAME = 'MySQL56'
    import win32service
    import win32serviceutil
    if win32serviceutil.QueryServiceStatus(MYSQL_WIN32_SERVICE_NAME)[1] == (
                win32service.SERVICE_RUNNING or win32service.SERVICE_START_PENDING):
        return True
    else:
        return False


def bring_up_mysql_service():
    import win32api
    import time
    MYSQL_WIN32_SERVICE_NAME = 'MySQL56'
    try:
        win32api.ShellExecute(0, 'runas', 'sc', 'start %s' % MYSQL_WIN32_SERVICE_NAME, '', 1)
        time.sleep(2)  # it is not essential
    except Exception as e:
        def get_system_encoding():
            import codecs
            import locale
            """
            The encoding of the default system locale but falls back to the given
            fallback encoding if the encoding is unsupported by python or could
            not be determined.  See tickets #10335 and #5846
            """
            try:
                encoding = locale.getdefaultlocale()[1] or 'ascii'
                codecs.lookup(encoding)
            except Exception as _:
                del _
                encoding = 'ascii'
            return encoding

        DEFAULT_LOCALE_ENCODING = get_system_encoding()
        print e
        print e.args
        print e.message
        if isinstance(e, Iterable):
            for item in list(e):
                if isinstance(item, str):
                    print item.decode(DEFAULT_LOCALE_ENCODING),
                else:
                    print item,
        raise RuntimeError


threadingPool = list()
threading_1 = threading.Thread(target=runserver)
threading_2 = threading.Thread(target=openWebBrowser)
threadingPool.append(threading_1)
threadingPool.append(threading_2)

if __name__ == '__main__':
    try:
        for thread in threadingPool:
            thread.setDaemon(False)
            thread.start()

        thread.join()
    except RuntimeError:
        print thread.exc_traceback
