from django.contrib import admin

# Register your models here.
from models import AuditEntry


@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    # https://stackoverflow.com/questions/37618473/how-can-i-log-both-successful-and-failed-login-and-logout-attempts-in-django
    list_display = ['time', 'action', 'username', 'ip', ]
    list_filter = ['action', ]
