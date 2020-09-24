from django.contrib import admin

# Register your models here.

from . import models

class YourModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', )

admin.site.register(models.Task, YourModelAdmin)