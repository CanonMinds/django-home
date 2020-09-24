from django.contrib.auth.models import User
from django.db import models

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

    activity = models.CharField(max_length=255)
    priority = models.CharField(choices=PRIORITY_RANKS, default=NORMALPRIORITY, max_length=3)

    def __str__(self):
        return self.activity


