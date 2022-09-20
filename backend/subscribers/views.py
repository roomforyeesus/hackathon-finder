from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Subscriber


def index(request):
    """returns subscribers in json format"""
    data=list(Subscriber.objects.all().values())
    return JsonResponse(data, safe=False)

def post_subscriber(request):
    """post subscribers to db"""
    print(request.POST)
    email = request.POST.get('email')
    name = request.POST.get('name')
    Subscriber.objects.create(email=email)
    Subscriber.objects.create(name=name)
    return HttpResponse('ok')