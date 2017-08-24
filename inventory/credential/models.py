# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid
from django.core.validators import EmailValidator, URLValidator


# https://docs.djangoproject.com/en/1.11/
# https://docs.djangoproject.com/en/1.11/ref/models/fields/
class Credentials(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Credentials"

    # learn from 1Password
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=45, null=False, verbose_name=u'Title', help_text=u'Title')
    url = models.CharField(max_length=45, default=None, null=True, blank=True, verbose_name=u'URL',
                           help_text=u'app url', validators=[URLValidator])

    username = models.CharField(max_length=45, null=False, verbose_name=u'username', help_text=u'username')
    display_name = models.CharField(max_length=45, blank=True, null=True, verbose_name=u'Display Name',
                                    help_text=u'alias,screenName,firstName lastName')
    loginname = models.CharField(max_length=45, null=False, verbose_name=u'Login Name', help_text=u'Login Name')
    real_password = models.CharField(max_length=45, null=False, verbose_name=u'real password',
                                     help_text=u'password in plain text')
    is_realname = models.NullBooleanField(default=False, blank=True, null=True, verbose_name=u'Is real name',
                                          choices=((True, u'Is real-name'), (False, u'Not real-name')),
                                          help_text=u'True, Is real-name; False, Not real-name')
    admin_console_url = models.CharField(max_length=45, default=None, null=True, blank=True,
                                         verbose_name=u'admin console URL',
                                         help_text=u'admin console URL')
    admin_console_username = models.CharField(max_length=45, default=None, null=True, blank=True,
                                              verbose_name=u'admin console username',
                                              help_text=u'admin console username')
    admin_console_password = models.CharField(max_length=45, default=None, null=True, blank=True,
                                              verbose_name=u'admin console password',
                                              help_text=u'admin console password')

    status = models.NullBooleanField(default=True, blank=True, null=True, verbose_name=u'status',
                                     choices=((True, u'In using'), (False, u'Discarded')),
                                     help_text=u'True, in using; False, Discarded')

    last_modified = models.DateTimeField(null=False, auto_now=True, verbose_name=u'last modified',
                                         help_text=u'last modified')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")
    keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'tags or keywords',
                                help_text=u'tags or keywords')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'notes or description',
                                   help_text=u'notes or description')

    def __str__(self):  # __unicode__ on Python 2
        return self.loginname + " @ " + self.url

    def __unicode__(self):
        return self.loginname + " @ " + self.url


class Items(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Items"

    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=45, null=False, verbose_name=u'Title', help_text=u'Title')
    url = models.CharField(max_length=45, default=None, null=True, blank=True, verbose_name=u'URL',
                           help_text=u'app url', validators=[URLValidator])
    keywords = models.CharField(max_length=255, null=False, verbose_name=u'tags or keywords',
                                help_text=u'tags or keywords')
    description = models.CharField(max_length=255, null=False, verbose_name=u'notes or description',
                                   help_text=u'notes or description')
    last_modified = models.DateTimeField(null=False, auto_now=True, verbose_name=u'last modified',
                                         help_text=u'last modified')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    def __unicode__(self):
        return self.title


class Passwords(models.Model):
    class Meta:
        # http://stackoverflow.com/questions/18659308/admin-site-appending-letter-s-to-end-of-each-model-table-name-on-django
        # https://docs.djangoproject.com/en/dev/ref/models/options/#verbose-name-plural
        verbose_name_plural = "Passwords"

    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=45, null=False, verbose_name=u'Title', help_text=u'Title')
    url = models.CharField(max_length=45, default=None, null=True, blank=True, verbose_name=u'URL',
                           help_text=u'app url', validators=[URLValidator])
    credential = models.ForeignKey('Credentials', to_field='uuid', on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255, null=False, verbose_name=u'tags or keywords',
                                help_text=u'tags or keywords')
    description = models.CharField(max_length=255, null=False, verbose_name=u'notes or description',
                                   help_text=u'notes or description')
    last_modified = models.DateTimeField(null=False, auto_now=True, verbose_name=u'last modified',
                                         help_text=u'last modified')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=u'Created on',
                                        help_text="Created on")

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    def __unicode__(self):
        return self.title
