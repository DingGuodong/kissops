from django.contrib import admin
from .models import Hosts


# Register your models here.
class HostsList(admin.ModelAdmin):
    list_display = ('hostname', 'type', 'private_ip',)
    search_fields = ('hostname', 'private_ip')


admin.site.register(Hosts, HostsList)
