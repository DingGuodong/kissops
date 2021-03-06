# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hosts_hosts', models.CharField(help_text='host name, IP address or name.', max_length=128)),
                ('hosts_type', models.IntegerField(default=0, help_text='0, UNIX/Linux; 1, Windows')),
                ('hosts_ip_public', models.CharField(help_text='public ip address', max_length=20)),
                ('hosts_ip_private', models.CharField(help_text='private ip address', max_length=20)),
                ('hosts_user', models.CharField(help_text='user name', max_length=20)),
                ('hosts_user_is_privilege',
                 models.IntegerField(default=0, help_text='0, root/with sudo; 1, normal user')),
                ('hosts_user_is_sudo', models.IntegerField(default=0, help_text='0, sudo; 1, non-sudo')),
                ('hosts_user_password', models.CharField(help_text='user password', max_length=128)),
            ],
        ),
    ]
