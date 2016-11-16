from __future__ import unicode_literals

from django.db import models
import uuid
from inventory.project.models import Projects


# Create your models here.
class Datacenters(models.Model):
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Datacenter Name',
                            help_text="Datacenter Name")
    # https://docs.djangoproject.com/en/1.10/ref/models/fields/
    project = models.ForeignKey(Projects, related_name=u'project_datacenter', blank=True, null=True,
                                on_delete=models.SET_NULL)
    network = models.TextField(blank=True, null=True, verbose_name=u"IP Network")
    bandwidth = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Band Width')
    type = models.IntegerField(verbose_name=u"Type",
                               choices=((0, 'cloud'), (1, 'physical'), (2, 'Mixed'), (3, 'Unknown')), blank=True,
                               null=True)
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"Address")
    operator = models.IntegerField(verbose_name=u"Operator",
                                   choices=((0, 'CU'), (1, 'CN'), (2, 'Cloud'), (3, 'Mixed'), (4, 'Unknown')),
                                   blank=True,
                                   null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")
    comment = models.TextField(blank=True, null=True, verbose_name=u"Comment")

    # using this for ForeignKey used by datacenter
    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return self.name
