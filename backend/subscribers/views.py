from tokenize import Token
from django.http import JsonResponse
from .models import Subscribers
from .timer import timer
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
        # print(data)
        email = data['email']
        name = data['name']
        new_subscriber = Subscribers(email=email, name=name)
        new_subscriber.save()
        print('new subscriber saved')
        timer()
        return JsonResponse('Email added', safe=False)

