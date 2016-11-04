#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:admin.py
User:               Guodong
Create Date:        2016/9/26
Create Time:        14:34
 """
from django.contrib import admin
from kissops.models import Hosts


class HostsList(admin.ModelAdmin):
    list_display = ('hosts_hosts', 'hosts_type', 'hosts_ip_private', )
    search_fields = ('hosts_hosts', 'hosts_ip_private')

admin.site.register(Hosts, HostsList)
