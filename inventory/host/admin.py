from django.contrib import admin
from .models import Hosts


# Register your models here.
class HostsList(admin.ModelAdmin):
    list_display = ('hosts_hosts', 'hosts_type', 'hosts_ip_private',)
    search_fields = ('hosts_hosts', 'hosts_ip_private')


admin.site.register(Hosts, HostsList)
