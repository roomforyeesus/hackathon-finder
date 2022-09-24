import os 
from dotenv import load_dotenv
from . models import Contests, Subscribers
from . import hackathonData
from trycourier import Courier
import requests
import json

load_dotenv()
APIKEY = os.getenv('courierapikey')
TESTKEY = os.getenv('courierapikeytest')



def sendEmail():
    print('hitting the sendEmail method')
    subs = Subscribers.objects.all()
    contest = Contests.objects.all()
    client = Courier(auth_token=APIKEY)
    resp = client.send_message(
  message={
    "to": {
      "email": "{{subs.email}}",
    },
    "content": {
      "title": "Welcome!",
      "body": "Thanks for signing up, {{subs.name}}! here's some hackathons you might be interested in: {{contest.name}},{{contest.url}}.{{contest.in_24_hours}} Good luck!",
    },
    "data": {
      "name": "{{subs.name}}",
    },
    "routing": {
      "method": "single",
      "channels": ["email"],
    },
  }
)

    print(resp['requestId'])

print('emails sent')
