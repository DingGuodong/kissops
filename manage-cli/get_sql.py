#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:get_sql.py
User:               Guodong
Create Date:        2017/8/23
Create Time:        16:01
Description:        
References:         http://luozhaoyu.iteye.com/blog/1510635
 """
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
try:
    app_name = raw_input("What app name would you like get SQL?\n")
    os.system("python manage.py dbshell  {name}".format(name=app_name))
except OSError as e:
    print e.message
    sys.exit(1)
