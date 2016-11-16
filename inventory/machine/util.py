#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:util.py
User:               Guodong
Create Date:        2016/11/15
Create Time:        17:02
 """


# Reg Refer: http://www.ziqiangxuetang.com/python/python-reg-expressions.html
def model_to_admin():
    import re
    result = list()
    with open('models.py', 'r') as f:
        for line in f:
            match = re.findall('\S+\w[^ ]+(?= = )', line)
            if match:
                result.append(match[0])
    if result:
        return tuple(result)
    else:
        return None


print model_to_admin()
