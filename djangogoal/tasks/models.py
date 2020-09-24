from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    activity = models.CharField(max_length=255)
    priority = models.PositiveIntegerField()

    def __str__(self):
        return self.activity


