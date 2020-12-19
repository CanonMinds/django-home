from django.contrib import admin

# Register your models here.
from .models import Province

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("city", "region", "products", "area")

admin.site.register(Province, ProvinceAdmin)