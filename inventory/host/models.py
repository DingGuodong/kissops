from __future__ import unicode_literals

from django.db import models
import uuid


# Create your models here.
class Hosts(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Hosts"

    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#uuidfield
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    hostname = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Hostname',
                                help_text="host name, IP address or name.")
    type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Type',
                               choices=((0, u'UNIX/Linux'), (1, u'Windows')),
                               help_text="0, UNIX/Linux; 1, Windows")
    public_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name=u'Public IP',
                                             help_text="public ip address")
    public_ip_secondary = models.GenericIPAddressField(max_length=20, blank=True, null=True,
                                                       verbose_name=u'Public IP Secondary',
                                                       help_text="public ip address secondary")
    private_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name=u'Private IP',
                                              help_text="private ip address")
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'Username', help_text="user name")
    is_privilege = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'Is Privilege',
                                           choices=((True, u'True'), (False, u'False')),
                                           help_text="True, root/with sudo; False, normal user")
    is_sudo = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'Is Sudo',
                                      choices=((True, u'True'), (False, u'False')),
                                      help_text="True, sudo; False, non-sudo")
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Password',
                                help_text="user password")

    # def __str__(self):  # __unicode__ on Python 2
    #     return self.hosts_hosts
    #
    # def __unicode__(self):
    #     return self.hosts_hosts
