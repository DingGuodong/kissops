#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:runserver.py
User:               Guodong
Create Date:        2016/9/26
Create Time:        10:34
 """
from gevent import monkey

monkey.patch_all()
import os
import sys
import gevent

admin_url = 'http://127.0.0.1:8000/admin/'
app_url = 'http://127.0.0.1:8000/admin/itoms/app/'


def runserver():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(BASE_DIR)
    try:
        print "Admin --> %s" % admin_url
        print "App   --> %s" % app_url
        gevent.sleep(0.2)
        # TODO(Guodong Ding) python non-blocking execute system command
        os.system("python manage.py runserver")  # blocking
    except OSError as e:
        print e.message
        sys.exit(1)


def openwebbrowser():
    import webbrowser
    webbrowser.open(app_url)
    webbrowser.open(admin_url)


gevent.joinall([gevent.spawn(runserver), gevent.spawn(openwebbrowser)])
