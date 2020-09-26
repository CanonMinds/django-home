from rest_framework import serializers

from . import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta: 
        extra_kwargs = {
            'start': {
                'write_only': True
            }
        }#start(i.e. email) is supplied by the user, but does not appear when requested
        fields = (
            'activity',
            'priority',
            'start',
            'created_at',
            'updated_at',
        )
        model = models.Task
