from rest_framework import serializers

from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }#(i.e. email) is supplied by the user, but does not appear/displayed when requested in via API
        fields = (
            'id',
            'task',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        model = models.Review

class TaskSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True) #Has a drawback -notscalable of loading many responses
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='apiv2:review-detail') #Has a drawback since will greatly increased in future. Not scalabale
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta: 
        extra_kwargs = {
            'start': {
                'write_only': True
            }
        }#start(i.e. email) is supplied by the user, but is not displayed when requested
        fields = (
            'id',
            'activity',
            'priority',
            'start',
            'reviews',
            'created_at',
            'updated_at',
        )
        model = models.Task