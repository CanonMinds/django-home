from django.contrib import admin

# Register your models here.
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "region", "products", "area")

admin.site.register(Location, LocationAdmin)