from django.contrib import admin
from .models import Datacenters


# Register your models here.
class DatacentersList(admin.ModelAdmin):
    list_display = (
    'uuid', 'name', 'project', 'network', 'bandwidth', 'type', 'address', 'operator', 'date_created', 'comment')
    list_filter = ('type', 'operator')
    search_fields = ('name', 'type',)


admin.site.register(Datacenters, DatacentersList)
