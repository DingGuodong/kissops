# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid
from inventory.host.models import Hosts


# Create your models here.
class Microservices(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Microservices"

    severity_level = (
        (0, u'Not classified'),
        (1, u'high'),
        (2, u'medium'),
        (3, u'low')
    )

    service_status = (
        (0, u'Active'),
        (1, u'Inactive')
    )

    service_access_type = (
        (0, u'Directly'),
        (1, u'Reverse Proxy')
    )

    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Name',
                            help_text="Microservices Name")
    description = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Description',
                                   help_text="Description")
    caption = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Caption',
                               help_text="Caption")
    severity = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Severity',
                                   choices=severity_level,
                                   help_text="Choose severity level on this service")
    status = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Status',
                                 choices=service_status,
                                 help_text="Choose status on this service")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")
    domain_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Domain Name',
                                   help_text="Domain Name")
    access_type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Status',
                                      choices=service_access_type,
                                      help_text="Choose status on this service")
    proxy_agent = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Proxy Server',
                                   help_text="Proxy Server")
    host = models.ForeignKey(Hosts, related_name=u'hosts_microservices', blank=True, null=True,
                             on_delete=models.SET_NULL)
    public_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name=u'Public IP',
                                             help_text="public ip address(Optional)")
    public_ip_secondary = models.GenericIPAddressField(max_length=20, blank=True, null=True,
                                                       verbose_name=u'Public IP Secondary',
                                                       help_text="public ip address secondary(Optional)")
    private_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name=u'Private IP',
                                              help_text="private ip address")
    ports = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Service Ports',
                             help_text="Service Ports, separate with comma")
    installation_path = models.TextField(blank=True, null=True, verbose_name=u"Installation Path",
                                         help_text=u"Installation Path")
    installation_description = models.TextField(blank=True, null=True, verbose_name=u"Installation Description",
                                                help_text=u"Installation Description")
    dependency_detail = models.TextField(blank=True, null=True, verbose_name=u"Service Dependency",
                                         help_text=u"Service Dependency")
    health_check = models.TextField(blank=True, null=True, verbose_name=u"Health Check", help_text=u"Health Check")
    health_description = models.TextField(blank=True, null=True, verbose_name=u"Health Check Description",
                                          help_text=u"Health Check Description")
    update_log = models.TextField(blank=True, null=True, verbose_name=u"Update Log", help_text=u"Update Log")
    url = models.URLField(max_length=200, blank=True, null=True, verbose_name=u'URL',
                          help_text="URL/Link(Optional)")
    username = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Username',
                                help_text="Username(Optional)")
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Password',
                                help_text="User password(Optional)")

    # using this for ForeignKey used by
    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return self.name
