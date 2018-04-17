#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File Name:              LinuxBashShellScriptForOps:util.py
Version:                0.0.1
Author:                 Guodong
Author Email:           dgdenterprise@gmail.com
URL:                    https://github.com/DingGuodong/LinuxBashShellScriptForOps
Download URL:           https://github.com/DingGuodong/LinuxBashShellScriptForOps/tarball/master
Create Date:            2018/3/13
Create Time:            13:46
Description:            
Long Description:       
References:             
Prerequisites:          []
Development Status:     3 - Alpha, 5 - Production/Stable
Environment:            Console
Intended Audience:      System Administrators, Developers, End Users/Desktop
License:                Freeware, Freely Distributable
Natural Language:       English, Chinese (Simplified)
Operating System:       POSIX :: Linux, Microsoft :: Windows
Programming Language:   Python :: 2.6
Programming Language:   Python :: 2.7
Topic:                  Utilities
 """

import json

import requests


def obtain_auth_token(username, password):
    url = "http://127.0.0.1:8000/api/api-token-auth/"

    payload = {
        "username": username,
        "password": password
    }

    payload = json.dumps(payload)

    headers = {
        'Content-Type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def validate_token():
    url = "http://127.0.0.1:8000/api/users/"

    headers = {
        'Authorization': "Token f7200ae9ed773c2b22f32acf8ff7a689e001b6db",
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


if __name__ == '__main__':
    user = raw_input("username: ")
    secret = raw_input("password:")
    obtain_auth_token(user, secret)
    validate_token()
