from __future__ import unicode_literals

from django.db import models
import uuid
from inventory.datacenter.models import Datacenters


# Create your models here.
class Devices(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Devices"

    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Name',
                            help_text="Device Name")
    datacenter = models.ForeignKey(Datacenters, related_name=u'datacenter_device', blank=True, null=True,
                                   on_delete=models.SET_NULL)
    type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Type',
                               choices=((0, u'Network Device'), (1, u'Security')),
                               help_text="0, Network Device; 1, Security")
    is_manageable = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'Is Manageable',
                                            choices=((True, u'True'), (False, u'False')),
                                            help_text="Is Manageable; False, Unmanageable")
    url = models.URLField(max_length=200, blank=True, null=True, verbose_name=u'URL',
                          help_text="URL/Link")
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'Username', help_text="Username")
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Password',
                                help_text="user password")
