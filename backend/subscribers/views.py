from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Subscriber


def index(request):
    """returns subscribers in json format"""
    data=list(Subscriber.objects.all().values())
    return JsonResponse(data, safe=False)

def post_subscriber(request):
    return HttpResponse('Hello World')
