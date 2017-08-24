#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:startapp.py
User:               Guodong
Create Date:        2016/9/27
Create Time:        10:26
Description:        Creates a Django app directory structure for the given app name in the current
                    directory or optionally in the given directory.
 """
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
try:
    print "BUILD APP ONCE, DELIVER IT ANYWHERE WITH MODIFY 'APPS.PY'."
    app_name = raw_input("What app name would you like create?\n")
    app_directory = raw_input("What app directory would you like give?\n")
    if app_name != "" and app_directory != '':
        if not os.path.exists(app_directory):
            print "directory your given does not exist, create it!"
            os.makedirs(app_directory)
        print "Creates a Django app directory structure for the given app name in the given directory."
        os.system("python manage.py startapp {name} {directory}".format(name=app_name, directory=app_directory))
    elif app_name != "" and app_directory == '':
        print "Creates a Django app directory structure for the given app name in the current directory "
        os.system("python manage.py startapp {name}".format(name=app_name))
    else:
        raise RuntimeError
except OSError as e:
    print e.message
    sys.exit(1)
