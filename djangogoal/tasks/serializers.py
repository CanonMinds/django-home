from django.db.models import Avg
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

    def validate_rating(self, value):
        if value in range(1,6):
            return value
        raise serializers.ValidationError(
        'Rating must be an integer between 1 and 5')

class TaskSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True) #Has a drawback -notscalable of loading many responses
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='apiv2:review-detail') #Has a drawback since will greatly increased in future. Not scalabale
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
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
            'average_rating',
        )
        model = models.Task
    
    def get_average_rating(self, obj):
        average = obj.reviews(Avg('rating')).get('rating__avg')

        if average is None:
            return 0

        return round(average*2) / 2