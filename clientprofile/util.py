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
    # print model_to_admin()
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


def uuid_to_hex(old_sql, new_sql):
    # uuid_to_hex("appasswd.sql", "new_appasswd.sql")
    import re
    import uuid
    with open(old_sql, 'r') as f:
        with open(new_sql, 'w') as nf:
            for line in f:
                match = re.findall(r'(([^-\']+-){4}[^-\']+)', line)
                if match:
                    print match[0][0], "-->", uuid.UUID(match[0][0]).get_hex()
                    newline = line.replace(match[0][0], uuid.UUID(match[0][0]).get_hex())
                    nf.write(newline)


def check_uuid(filename):
    # check_uuid("filename1")
    import uuid
    with open(filename, 'r') as f:
        for value in f:
            if value is not None:
                try:
                    uuid.UUID(value)
                except ValueError:
                    print value.strip()
            else:
                print value


def gen_uuid(number, filename="uuid_list.txt", on_screen=True):
    import uuid
    if on_screen:
        for x in xrange(number):
            print uuid.uuid4().get_hex()
    else:
        with open(filename, 'w') as f:
            for x in xrange(number):
                if x:
                    f.write(uuid.uuid4().get_hex() + '\n')
            f.flush()


if __name__ == '__main__':
    print model_to_admin()
