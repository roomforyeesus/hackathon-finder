from tokenize import Token
from django.http import JsonResponse
from .models import Subscribers, Contests
from .timer import timer
from .sendEmails import confEmail
import json
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class SubscriberView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    print('hitting the post method')
    def post(self, request):
        print('hitting the post method')
        data = json.loads(request.body)
        print(data)
        email = data['email']
        name = data['name']
        phone_number = data['phone_number']
        new_subscriber = Subscribers(email=email, name=name, phone_number=phone_number)
        new_subscriber.save()
        print('new subscriber saved')
        confEmail(data)
        timer()
        return JsonResponse('Email added', safe=False)
    
    # def getHackathons(self, request):
    #     print('hitting the get method')
    #     contests = Contests.objects.all()
    #     print(contests)
    #     return JsonResponse('Hackathons', safe=False)
