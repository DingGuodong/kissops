from __future__ import unicode_literals

from django.db import models
import uuid
from inventory.machine.models import Machines


# Create your models here.
class Hosts(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Hosts"

    boolean_choices = ((True, u'True'), (False, u'False'))

    os_family_choices = (
        (0, "Linux"),
        (1, "CentOS"),
        (101, "CentOS 6"),
        (102, "CentOS 7"),
        (2, "Ubuntu"),
        (201, "Ubuntu 14"),
        (202, "Ubuntu 16"),
        (3, "Debian"),
        (301, "Debian 7"),
        (302, "Debian 8"),
        (4, "SUSE Linux"),
        (5, "OpenSUSE"),
        (6, "CoreOS"),
        (7, "FreeBSD"),
        (500, "Microsoft Windows"),
        (530, "Windows 10"),
        (527, "Windows 7 x64"),
        (526, "Windows 7"),
        (518, "Windows Server 2016"),
        (517, "Windows Server 2012"),
        (515, "Windows Server 2008 R2 x64"),
        (503, "Windows Server 2008 x64"),
        (510, "Windows Server 2003"),
        (1001, "Others")
    )

    environment_type_choices = (
        (0, "Production"),
        (1, "Development"),
        (2, "Test"),
    )

    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#uuidfield
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    instance_id = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Instance ID',
                                   help_text="Instance ID")
    hostname = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Hostname',
                                help_text="host name, IP address or name")
    is_virtual = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'Is Virtual',
                                         choices=boolean_choices,
                                         help_text="Is Virtual ot Physical")
    machine = models.ForeignKey(Machines, related_name=u'machines_hosts', blank=True, null=True,
                                on_delete=models.SET_NULL)
    environment_type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Environment Type',
                                           help_text="Production or Test or Development",
                                           choices=environment_type_choices)
    availability_zone = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Availability Zone',
                                         help_text="Availability Zone")
    type = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Type',
                               choices=os_family_choices,
                               help_text="UNIX/Linux or Windows")
    public_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name=u'Public IP',
                                             help_text="public ip address")
    public_ip_secondary = models.GenericIPAddressField(max_length=20, blank=True, null=True,
                                                       verbose_name=u'Public IP Secondary',
                                                       help_text="public ip address secondary")
    private_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name=u'Private IP',
                                              help_text="private ip address")
    cpu_cores = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Number of CPUs cores',
                                    help_text="Number of CPUs cores")
    memory_size = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Memory Size(MB)',
                                      help_text="Memory Size(MB)")
    bandwidth = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'BandWidth (MB)',
                                    help_text="BandWidth (MB)'")

    usage_purpose = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'usage purpose',
                                     help_text="usage purpose")
    description = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'description  or detail',
                                   help_text="description or detail")
    management_port = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Management Port',
                                          help_text="Management Port")
    console_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'console password',
                                        help_text="console password")
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'Username', help_text="user name")
    is_privilege = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'Is Privilege',
                                           choices=boolean_choices,
                                           help_text="True, root/with sudo; False, normal user")
    is_sudo = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'Is Sudo',
                                      choices=boolean_choices,
                                      help_text="True, sudo; False, non-sudo")
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Password',
                                help_text="user password")
    last_modified = models.DateTimeField(null=False, auto_now=True, verbose_name=u'last modified',
                                         help_text=u'last modified')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")

    def __str__(self):  # __unicode__ on Python 2
        return self.hostname

    def __unicode__(self):
        return self.hostname
