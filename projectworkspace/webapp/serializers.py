from rest_framework import serializers
from .models import User, ActivityPeriod


class activityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityPeriod
        fields=('start_time','end_time')

class userSerializer(serializers.ModelSerializer):
    activity_periods=activityPeriodSerializer(ActivityPeriod.objects.all(),many=True)
    class Meta:
        model=User
        fields=('id','real_name','tz','activity_periods')