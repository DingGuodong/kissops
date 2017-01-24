#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:rsync_static.py
User:               Guodong
Create Date:        2017/1/22
Create Time:        11:16
 """
from fabric.api import *
from fabric.contrib import project
import os

TOP_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Where the static files get collected locally. Your STATIC_ROOT setting.
env.local_static_root = 'C:\Users\Guodong\PycharmProjects\kissops\static'

# Where the static files should go remotely
env.remote_static_root = '/home/docker/volatile/static'

env.roledefs = {
    'static': ['10.20.0.129']
}


@roles('static')
def deploy_static():
    lcd(TOP_DIR)
    local('python ./manage.py collectstatic')
    project.rsync_project(
        remote_dir=env.remote_static_root,
        local_dir=env.local_static_root,
        delete=True,
    )
