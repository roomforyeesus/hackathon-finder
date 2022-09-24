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
    contests = Contests.objects.all()
    contestNow = []
    for contest in contests:
        if contest.status == 'BEFORE':
            contestNow = contest
            break
    subscribers = Subscribers.objects.all()
    client = Courier(auth_token=TESTKEY)
    for subscriber in subscribers:
              resp = client.send_message(
                message={
                  "to": {
                    "email": subscriber.email,
                  },
                  "content": {
                   "title": "Hackathon Alert",
                   "body": "Hackathon " + contestNow.name + " is starting soon! Click the link to register: " + contestNow.url,
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
              print (resp)
              print(resp['requestId'])
            
    print('emails sent to all subscribers')