from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Hosts(models.Model):
    hosts_hosts = models.CharField(primary_key=True, max_length=128, help_text="host name, IP address or name.")
    hosts_type = models.IntegerField(default=0, help_text="0, UNIX/Linux; 1, Windows")
    hosts_ip_public = models.CharField(max_length=20, help_text="public ip address")
    hosts_ip_private = models.CharField(max_length=20, help_text="private ip address")
    hosts_user = models.CharField(max_length=20, help_text="user name")
    hosts_user_is_privilege = models.IntegerField(default=0, help_text="0, root/with sudo; 1, normal user")
    hosts_user_is_sudo = models.IntegerField(default=0, help_text="0, sudo; 1, non-sudo")
    hosts_user_password = models.CharField(max_length=128, help_text="user password")

    # def __str__(self):  # __unicode__ on Python 2
    #     return self.hosts_hosts
    #
    # def __unicode__(self):
    #     return self.hosts_hosts
