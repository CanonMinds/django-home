from django.contrib import admin

# Register your models here.
from .models import Location, TestLocation

class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "region", "products", "area")
    list_filter = ("region", )
    search_fields = ("city", "region", "products", "area")

class TestLocationAdmin(admin.ModelAdmin):
    list_display = ("address", )

admin.site.register(Location, LocationAdmin)
admin.site.register(TestLocation, TestLocationAdmin)