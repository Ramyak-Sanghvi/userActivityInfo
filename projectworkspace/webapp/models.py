from django.db import models

# Create your models here.

class ActivityPeriod(models.Model):
    start_time=models.TextField()
    end_time=models.TextField()

    def __str__(self):
        return self.start_time
    
class User(models.Model):
    id=models.CharField(primary_key=True,max_length=9)
    real_name=models.CharField(max_length=25)
    tz=models.CharField(max_length=25)
    activity_periods=models.ManyToManyField(ActivityPeriod)
