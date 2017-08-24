# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from inventory.credential.models import Credentials, Items, Passwords
from django.core import urlresolvers


class ItemsList(admin.ModelAdmin):
    list_display = (
        'uuid', 'title', 'url', 'keywords', 'description', 'last_modified', 'date_created'
    )

    list_editable = (
        'title', 'url', 'keywords', 'description'
    )
    list_display_links = ('uuid',)
    search_fields = ("title", "keywords", " description",)
    list_filter = ("title",)
    list_per_page = 5
    actions_on_top = True
    save_on_top = True
    ordering = ("date_created",)


class CredentialsList(admin.ModelAdmin):
    list_display = (
        'uuid', 'username', 'display_name', 'loginname', 'real_password', 'is_realname',
        'admin_console_url', 'admin_console_username', 'admin_console_password', 'status', 'last_modified',
        'date_created',
    )

    list_editable = ('username', 'display_name', 'loginname', 'real_password', 'is_realname',
                     'admin_console_url', 'admin_console_username', 'admin_console_password', 'status'
                     )
    list_display_links = ('uuid',)
    search_fields = ("title",)
    list_filter = ("title",)
    list_per_page = 5
    actions_on_top = True
    save_on_top = True
    ordering = ("date_created",)


class PasswordsList(admin.ModelAdmin):
    # django add links to Foreign Key
    # Link in django admin to foreign key object
    # https://stackoverflow.com/questions/28832897/link-in-django-admin-to-foreign-key-object
    def credentials(self, obj):
        link = urlresolvers.reverse("admin:credential_credentials_change", args=[obj.credential.uuid])
        return u'<a href="%s">%s</a>' % (link, obj.credential.loginname)

    credentials.allow_tags = True
    list_display = (
        'uuid', 'title', 'url', 'credentials', 'keywords', 'description', 'last_modified', 'date_created'
    )
    list_editable = (
        'title', 'url', 'keywords', 'description'
    )
    list_display_links = ('uuid',)
    search_fields = ("title", "keywords", " description",)
    list_filter = ("title",)
    list_per_page = 5
    actions_on_top = True
    save_on_top = True
    ordering = ("date_created",)


admin.site.register(Credentials, CredentialsList)
admin.site.register(Items, ItemsList)
admin.site.register(Passwords, PasswordsList)
