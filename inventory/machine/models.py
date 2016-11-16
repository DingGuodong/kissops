from __future__ import unicode_literals

from django.db import models
import uuid
from inventory.datacenter.models import Datacenters


# Create your models here.
# grep -Po '\s+\K[^ ]+(?= \= )' model.py | awk 'BEGIN{printf "("}{printf "\047"$0"\047,"}END{printf ")"}'
class Machines(models.Model):
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Machine Name',
                            help_text="Machine Name")
    datacenter = models.ForeignKey(Datacenters, related_name=u'datacenter_machine', blank=True, null=True,
                                   on_delete=models.SET_NULL)
    type = models.IntegerField(verbose_name=u"Type", choices=((0, 'amd64'), (1, 'i386')), blank=True,
                               null=True)
    bios_release_date = models.DateTimeField(max_length=128, blank=True, null=True, verbose_name=u'BIOS release date',
                                             help_text="BIOS release date")
    bios_vendor = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'BIOS Vendor',
                                   help_text="BIOS Vendor")
    bios_version = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'BIOS Version',
                                    help_text="BIOS Version")
    block_devices = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Block Devices',
                                     help_text="Block Devices")
    block_device_model = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Block Device Model',
                                          help_text="Block Device Model")
    block_device_vendor = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Block Device Vendor',
                                           help_text="Block Device Vendor")
    block_device_size = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Block Device Size',
                                         help_text="Block Device Size")

    interfaces = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Interfaces',
                                  help_text="Interfaces")
    mac_address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'MAC Address',
                                   help_text="MAC Address")

    manufacturer = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Manufacturer',
                                    help_text="Manufacturer")
    product_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Product Name',
                                    help_text="Product Name")

    physical_processor_count = models.IntegerField(blank=True, null=True,
                                                   verbose_name=u'Physical Processor Count',
                                                   help_text="Physical Processor Count")
    processor_count = models.IntegerField(blank=True, null=True, verbose_name=u'Processor Count',
                                          help_text="Processor Count")
    processor = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Processor',
                                 help_text="Processor")
    memory_size = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Memory Size',
                                   help_text="Memory Size")
    memory_total = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Memory Total',
                                    help_text="Memory Total")
    domain = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Domain Name',
                              help_text="Domain Name")
    fqdn = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'FQDN Name',
                            help_text="FQDN Name")
    hostname = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Hostname',
                                help_text="Hostname")
    date_guarantee = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Guarantee',
                                          help_text="Guarantee")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")
    serial_number = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Serial Number',
                                     help_text="Serial Number")
    hardware_isa = models.IntegerField(choices=((0, 'amd64'), (1, 'i386')), blank=True, null=True,
                                       verbose_name=u'Processor Type',
                                       help_text="the processor type, uname -p")
    hardware_model = models.IntegerField(choices=((0, 'amd64'), (1, 'i386')), blank=True, null=True,
                                         verbose_name=u'Machine Name',
                                         help_text="the machine hardware name, uname -m")
    architecture = models.IntegerField(choices=((0, 'amd64'), (1, 'i386')), blank=True, null=True,
                                       verbose_name=u'Hardware Platform',
                                       help_text="the hardware platform ")
    ipaddress = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'IP Address',
                                 help_text="IP Address")
    netmask = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Netmask',
                               help_text="Netmask")
    network = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Network',
                               help_text="Network")
    is_virtual = models.NullBooleanField(choices=((0, True), (1, False)), blank=True, null=True,
                                         verbose_name=u'Is Virtual',
                                         help_text="Is Virtual")
    parent = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Parent',
                              help_text="Parent host if is virtual")
    operating_system = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Operating System',
                                        help_text="Operating System")
    operating_system_release = models.CharField(max_length=128, blank=True, null=True,
                                                verbose_name=u'Operating System Release',
                                                help_text="Operating System Release")
    os_family = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'OS Family',
                                 help_text="OS Family")
    comment = models.TextField(blank=True, null=True, verbose_name=u"Comment")
