#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:models.py
User:               Guodong
Create Date:        2016/7/9
Create Time:        17:02
 """

from django.db import models


class Hosts(models.Model):
    hosts_hosts = models.CharField(max_length=128, help_text="host name, IP address or name.")
    hosts_type = models.IntegerField(default=0, help_text="0, UNIX/Linux; 1, Windows")
    hosts_ip_public = models.CharField(max_length=20, help_text="public ip address")
    hosts_ip_private = models.CharField(max_length=20, help_text="private ip address")
    hosts_user = models.CharField(max_length=20, help_text="user name")
    hosts_user_is_privilege = models.IntegerField(default=0, help_text="0, root/with sudo; 1, normal user")
    hosts_user_is_sudo = models.IntegerField(default=0, help_text="0, sudo; 1, non-sudo")
    hosts_user_password = models.CharField(max_length=128, help_text="user password")

    def __str__(self):
        return self.hosts_hosts
