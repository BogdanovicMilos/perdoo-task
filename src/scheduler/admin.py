from django.contrib import admin
from scheduler.models import Scheduler


class SchedulerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'url', 'date', 'status']


admin.site.register(Scheduler, SchedulerAdmin)