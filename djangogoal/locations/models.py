from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=20)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    products = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "provinces"

    def __str__(self):
        return self.name