#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:views.py
User:               Guodong
Create Date:        2016/7/9
Create Time:        16:41
 """
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    username = request.user.username
    return render_to_response('index.html', {'username': username})
