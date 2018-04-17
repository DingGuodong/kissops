from __future__ import unicode_literals

import django.utils.timezone
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db import models
from django.dispatch import receiver


# Create your models here.


class AuditEntry(models.Model):
    # https://stackoverflow.com/questions/37618473/how-can-i-log-both-successful-and-failed-login-and-logout-attempts-in-django
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    time = models.DateTimeField(null=False, default=django.utils.timezone.now)

    def __unicode__(self):
        return '{0} - {1} - {2} - {3}'.format(self.time, self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user.username)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_out', ip=ip, username=user.username)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username', None))
