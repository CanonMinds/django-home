from django.contrib import admin

# Register your models here.

from . import models

class PlayerInline(admin.TabularInline):
    model = models.Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'position', 'age']


class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]

admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Player, PlayerAdmin)