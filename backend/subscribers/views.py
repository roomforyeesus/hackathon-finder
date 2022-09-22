from tokenize import Token
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Subscriber
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
        new_subscriber = Subscriber(email=email, name=name)
        new_subscriber.save()
        return JsonResponse('Email added', safe=False)
