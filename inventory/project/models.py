from __future__ import unicode_literals

from django.db import models
import uuid


# Create your models here.
class Projects(models.Model):
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Project Name',
                            help_text="Project Name")
    alias = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Project Alias Name',
                             help_text="Project Alias Name")
    namespace = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Namespace',
                                 help_text="Namespace")
    owner = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Owned by',
                             help_text="Project owner")
    creator = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Created by',
                               help_text="Created by")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")
    access = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Access',
                              help_text="Access")
    member = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Project Member',
                              help_text="Project Member")

    # using this for ForeignKey used by datacenter
    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def __unicode__(self):
        return self.name
