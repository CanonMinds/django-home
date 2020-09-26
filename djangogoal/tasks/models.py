from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.


class Task(models.Model):
    HIGHPRIORITY = "HP"
    NORMALPRIORITY = "NP"
    LOWPRIORITY = "LP"
    EMERGENCY = "SOS"
    RESCHEDULE = "RS"
    PRIORITY_RANKS = [
    (HIGHPRIORITY, 'High Priority'),
    (NORMALPRIORITY, 'Normal Priority'),
    (LOWPRIORITY, 'Low Priority'),
    (EMERGENCY, 'Emergency'),
    (RESCHEDULE, 'Reschedule'),
]

    activity = models.CharField(max_length=255, default='')
    priority = models.CharField(choices=PRIORITY_RANKS, default=NORMALPRIORITY, max_length=3)
    start = models.TimeField(default=datetime.time(8, 00))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity

class Review(models.Model):
    task = models.ForeignKey(Task, related_name='reviews', on_delete=models.DO_NOTHING )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['email','task']

    def __str__(self):
        return '{0.rating} by {0.email} for {0.task}'.format(self)

