from email import message
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

def confEmail(data):
    client = Courier(auth_token=TESTKEY)
    resp = client.send_message(
                message={
                  "to": {
                    "email": data['email'],
                  },
                  "content": {
                   "title": "Hackathon Alert",
                   "body": "Hi "+ data['name'] +"! You have successfully subscribed to Hackathon Alert. We will send you an email Monday to Wednesday when a hackathon starts in the next 24 hours.",
                  },
                  "data": {
                    "name": data['name'],
                  },
                  "routing": {
                    "method": "single",
                    "channels": ["email"],
                  },
                }
              )
    print(resp['requestId'])
    print('email sent to NEW subscriber')
    
def sendEmail():
    client = Courier(auth_token=TESTKEY)
    contests = Contests.objects.all()
    subscribers = Subscribers.objects.all()
    for contest in contests:
        if contest.in_24_hours == 'YES' and contest.status == 'BEFORE':
            for subscriber in subscribers:
                resp = client.send_message(
                    message={
                      "to": {
                        "email": subscriber.email,
                      },
                      "content": {
                       "title": "Hackathon Alert",
                       "body": "Hi "+ subscriber.name +"! A hackathon called "+ contest.name +" is starting in the next 24 hours. Check it out at "+ contest.url,
                      },
                      "data": {
                        "name": subscriber.name,
                      },
                      "routing": {
                        "method": "single",
                        "channels": ["email"],
                      },
                    }
                  )
                print(resp['requestId'])
                print('email sent to subscriber')