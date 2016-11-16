from django.contrib import admin
from .models import Hosts


# Register your models here.
class HostsList(admin.ModelAdmin):
    list_display = (
    'uuid', 'hostname', 'type', 'private_ip', 'public_ip', 'username', 'password', 'is_privilege', 'is_sudo',)
    list_filter = ('type',)
    search_fields = ('hostname', 'private_ip', 'public_ip')


admin.site.register(Hosts, HostsList)
