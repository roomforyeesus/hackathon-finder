from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Subscriber
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class SubscriberView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """get subscribers from db"""
        subscribers = Subscriber.objects.all()
        subscribers_list = []
        for subscriber in subscribers:
            subscribers_list.append({'email': subscriber.email, 'name': subscriber.name})
        return Response(subscribers_list)

    def post(self, request, format=None):
        """post subscribers to db"""
        print(request.data)
        email = request.data.get('email')
        name = request.data.get('name')
        Subscriber.objects.create(email=email)
        Subscriber.objects.create(name=name)
        return Response('ok')

