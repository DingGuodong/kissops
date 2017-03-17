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


def openwebbrowser():
    import webbrowser
    import time
    while True:
        if is_port_open('127.0.0.1', 8000):
            webbrowser.open(app_url)
            webbrowser.open(admin_url)
            break
        else:
            time.sleep(0.2)


threadingPool = list()
threading_1 = threading.Thread(target=runserver)
threading_2 = threading.Thread(target=openwebbrowser)
threadingPool.append(threading_1)
threadingPool.append(threading_2)

if __name__ == '__main__':
    for thread in threadingPool:
        thread.setDaemon(False)
        thread.start()

    thread.join()
