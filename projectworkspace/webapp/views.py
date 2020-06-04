from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, ActivityPeriod
from rest_framework.renderers import JSONRenderer
from .serializers import userSerializer, activityPeriodSerializer

# Create your views here.

class UserActivityInfo(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        try:
            """
            #dummy data insertion code
            import string,random
            real_name=["Egon Spengler","Glinda Southgood","Ramyak Sanghvi","Raj Sanghvi"]
            tz=['America/Los_Angeles','Asia/Kolkata']
            letters = string.ascii_letters + string.digits
            for i in range(4):
                id=''.join(random.choice(letters) for i in range(9))
                user=User(id=id,real_name=real_name[i],tz=tz[i%2])
                user.save()
            start_times=["Feb 1 2020  1:33PM","Mar 1 2020  11:11AM","Mar 16 2020  5:33PM","Mar 21 2020  5:33PM"]
            end_times=["Feb 1 2020 1:54PM","Mar 1 2020 2:00PM","Mar 16 2020 8:02PM","Mar 21 2020 8:02PM"]
            from random import randrange
            for i in range(randrange(4)):
                activityPeriod=ActivityPeriod(start_time=start_times[i],end_time=end_times[i])
                activityPeriod.save()
            users=User.objects.all()
            for user in users:
                for activityPeriod in ActivityPeriod.objects.all():
                    user.activity_periods.add(activityPeriod)
            """
            users=User.objects.all()
            serializer=userSerializer(users, many=True)

            return Response({
                "ok": True,
                "members":serializer.data
            })
        except Exception as ex:
            print(ex)
