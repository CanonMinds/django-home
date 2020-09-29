from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
ACTIVITIES = (
    ('T1', 'Standby'),
    ('T2', 'Research'),
    ('T3', 'Field'),
)

class Team(models.Model):
    name = models.CharField(max_length=255)
    lead = models.ForeignKey(User, related_name='teams', on_delete=models.PROTECT)
    field_location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):    
        return reverse("teams:detail", kwargs={"pk": self.pk})

class Status_detail(models.Model):
    detail = models.CharField(max_length=255)
    months_active = models.PositiveIntegerField()
    activity = models.CharField(choices=ACTIVITIES, max_length=3)
    team = models.ForeignKey(Team, related_name='status', on_delete=models.PROTECT, default='')

    def __str__(self):
        return self.detail
