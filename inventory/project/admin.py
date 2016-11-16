from django.contrib import admin
from .models import Projects


# Register your models here.
class ProjectsList(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'alias', 'namespace', 'owner', 'creator', 'date_created', 'access', 'member',)
    list_filter = ('namespace', 'owner', 'creator',)
    search_fields = ('name', 'alias',)


admin.site.register(Projects, ProjectsList)
