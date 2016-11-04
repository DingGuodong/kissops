#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:startapp.py
User:               Guodong
Create Date:        2016/9/27
Create Time:        10:26
 """
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
try:
    app_name = raw_input("What app name would you like create?\n")
    if app_name != "":
        os.system("python manage.py startapp %s" % app_name)
    else:
        raise RuntimeError
except OSError as e:
    print e.message
    sys.exit(1)
