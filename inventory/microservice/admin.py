# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from inventory.microservice.models import Microservices


class MicroservicesList(admin.ModelAdmin):
    list_display = (
        'uuid', 'name', 'description', 'caption', 'severity', 'status', 'date_created', 'domain_name', 'access_type',
        'proxy_agent', 'host', 'public_ip', 'public_ip_secondary', 'private_ip', 'ports', 'installation_path',
        'installation_description', 'dependency_detail', 'health_check', 'health_description', 'update_log', 'url',
        'username', 'password')

    list_editable = (
        'name', 'description', 'caption', 'severity', 'status', 'domain_name', 'access_type',
        'proxy_agent', 'host', 'public_ip', 'public_ip_secondary', 'private_ip', 'ports', 'installation_path',
        'installation_description', 'dependency_detail', 'health_check', 'health_description', 'update_log', 'url',
        'username', 'password')
    list_display_links = ('uuid',)
    search_fields = ("name", "description", " domain_name", "installation_description")
    list_filter = ("name",)
    list_per_page = 5
    actions_on_top = True
    save_on_top = True
    ordering = ("date_created",)


admin.site.register(Microservices, MicroservicesList)
