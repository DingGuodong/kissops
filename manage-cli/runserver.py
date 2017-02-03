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
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
print "Admin --> http://127.0.0.1:8000/admin/"
print "App   --> http://127.0.0.1:8000/admin/itoms/app/"
try:
    os.system("python manage.py runserver")
except OSError as e:
    print e.message
    sys.exit(1)
