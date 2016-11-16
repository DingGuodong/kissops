from django.contrib import admin
from .models import Machines


# Register your models here.
class MachinesList(admin.ModelAdmin):
    list_display = (
        'uuid', 'name', 'datacenter', 'type', 'bios_release_date', 'bios_vendor', 'bios_version', 'block_devices',
        'block_device_model', 'block_device_vendor', 'block_device_size', 'interfaces', 'mac_address', 'manufacturer',
        'product_name', 'physical_processor_count', 'processor_count', 'processor', 'memory_size', 'memory_total',
        'domain', 'fqdn', 'hostname', 'date_guarantee', 'date_created', 'serial_number', 'hardware_isa',
        'hardware_model', 'architecture', 'ipaddress', 'netmask', 'network', 'is_virtual', 'parent', 'operating_system',
        'operating_system_release', 'os_family', 'comment',)
    list_filter = ('type', 'datacenter', 'domain', 'fqdn', 'hostname', 'is_virtual', 'parent',)
    search_fields = ('type', 'datacenter', 'domain', 'fqdn', 'hostname', 'is_virtual', 'parent',)


admin.site.register(Machines, MachinesList)
