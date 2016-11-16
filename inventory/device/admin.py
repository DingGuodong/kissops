from django.contrib import admin
from .models import Devices


# Register your models here.
class DevicesList(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'datacenter', 'type', 'is_manageable', 'url', 'username', 'password',)
    list_display_links = ('uuid',)
    list_filter = ('type',)
    search_fields = ('name', 'type',)
    list_editable = ('name', 'datacenter', 'type', 'is_manageable', 'url', 'username', 'password',)


admin.site.register(Devices, DevicesList)
