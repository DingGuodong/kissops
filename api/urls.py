#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:urls.py
User:               Guodong
Create Date:        2017/9/15
Create Time:        16:32
Description:        
References:         
Prerequisites:      []
 """
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as token_views

from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the viewable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', token_views.obtain_auth_token)
]
