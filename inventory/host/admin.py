from django.contrib import admin
from .models import Hosts


# Register your models here.
class HostsList(admin.ModelAdmin):
    list_display = (
        'uuid', 'instance_id', 'hostname', 'environment_type', 'availability_zone', 'is_virtual', 'machine',
        'public_ip', 'public_ip_secondary',
        'private_ip', 'cpu_cores', 'memory_size', 'bandwidth', 'usage_purpose', 'description', 'type',
        'management_port', 'console_password', 'username', 'is_privilege', 'is_sudo', 'password', 'last_modified',
        'date_created'
    )

    list_filter = ('availability_zone', 'environment_type',)
    search_fields = ('hostname', 'public_ip', 'private_ip', 'instance_id',)

    list_editable = (
        'hostname', 'environment_type', 'availability_zone', 'is_virtual', 'machine',
        'public_ip', 'public_ip_secondary',
        'private_ip', 'cpu_cores', 'memory_size', 'bandwidth', 'usage_purpose', 'description', 'type',
        'management_port', 'console_password', 'username', 'is_privilege', 'is_sudo', 'password',
    )
    list_display_links = ('uuid',)
    list_per_page = 5
    actions_on_top = True
    save_on_top = True
    ordering = ("date_created",)


admin.site.register(Hosts, HostsList)
