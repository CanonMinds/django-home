from django.db import models

# Create your models here.
class Province(models.Model):
    city = models.CharField("City/Municipality", max_length=255, null=True, blank=True)
    region = models.CharField(max_length=55, null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    products = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
      verbose_name_plural = "provinces"

    def __str__(self):
        return self.city

class Location(models.Model):
    city = models.CharField("City/Municipality", max_length=255, null=True, blank=True)
    region = models.CharField(max_length=55, null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    products = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
      verbose_name_plural = "locations"

    def __str__(self):
        return self.city

class TestLocation(models.Model):
    address = models.CharField("Address", max_length=255, null=True, blank=True)

    class Meta:
      verbose_name_plural = "testlocations"

    def __str__(self):
        return self.address
    