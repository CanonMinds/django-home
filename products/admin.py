from django.contrib import admin

from .models import *
from . import models

# Register your models here.
class OrderInline(admin.TabularInline):
    model = models.Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'complete', 'transaction_id']

class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)