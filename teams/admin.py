from django.contrib import admin

# Register your models here.

from . import models

class StatusInline(admin.TabularInline):
    model = models.Status_detail


class StatusAdmin(admin.ModelAdmin):
    list_display = ['detail', 'team', 'activity', 'months_active']


class TeamAdmin(admin.ModelAdmin):
    inlines = [StatusInline]

admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Status_detail, StatusAdmin)