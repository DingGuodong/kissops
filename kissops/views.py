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
from django.http import HttpResponse
from django.shortcuts import render
from models import Hosts


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def list_hosts(request):
    hosts = Hosts.objects.order_by('-hosts_hosts')[:10]
    return render(request, 'hosts.html', {'hosts': hosts})


def current_datetime(request):
    import datetime
    now = datetime.datetime.now()
    html = "It is now %s." % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    from django.http import Http404
    import datetime
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)


def send_email(request):
    from django.conf import settings
    from django.core.mail import send_mail
    send_mail('Subject', 'message.', settings.DEFAULT_FROM_EMAIL,
              ['dinggd@huntor.cn'], fail_silently=False)
    return HttpResponse("email send!")
