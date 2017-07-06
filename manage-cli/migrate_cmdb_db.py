#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:migrate_cmdb_db.py
User:               Guodong
Create Date:        2017/7/5
Create Time:        17:35
Description:        
 """
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)
try:
    os.system("python manage.py makemigrations cmdb")
    os.system("python manage.py migrate cmdb --database=cmdb_db")
except OSError as e:
    print e.message
    sys.exit(1)
