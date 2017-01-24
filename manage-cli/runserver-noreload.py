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

ENABLE_DEBUG_SAVED = os.getenv('ENABLE_DEBUG')
RUN_ENVIRONMENT_SAVED = os.getenv('RUN_ENVIRONMENT')
os.environ['ENABLE_DEBUG'] = 'False'
os.environ['RUN_ENVIRONMENT'] = 'local'

print 'Enable debug: %s' % os.getenv('ENABLE_DEBUG')
print 'Django setting: %s' % os.getenv('RUN_ENVIRONMENT')

try:
    os.system("python manage.py runserver --noreload")
except OSError as e:
    print e.message
    sys.exit(1)
except (KeyboardInterrupt, SystemExit) as e:
    print e
    sys.exit(1)
finally:
    os.environ['ENABLE_DEBUG'] = ENABLE_DEBUG_SAVED
    os.environ['RUN_ENVIRONMENT'] = RUN_ENVIRONMENT_SAVED
