from email import message
import os 
from dotenv import load_dotenv
from . models import Contests, Subscribers
from . import hackathonData
from trycourier import Courier

load_dotenv()
APIKEY = os.getenv('courierapikey')
TESTKEY = os.getenv('courierapikeytest')

def confEmail(data):
    client = Courier(auth_token=TESTKEY)
    resp = client.send_message(
                message={
                  "to": {
                    "phone_number": data['phone_number'],
                    "email": data['email'],
                  },
                  "content": {
                   "title": "Hackathon Alert",
                   "body": "Hiya "+ data['name'] +"! You have successfully subscribed to Hackathon Finder's Alerts. We will send you an email periodicly when a hackathon is starting in the next 24 hours.",
                  },
                  "data": {
                    "name": data['name'],
                  },
                  "routing": {
                    "method": "all",
                    "channels": ["sms", "email"],
                  },
                }
              )
    print(resp['requestId'])
    print('messeges sent to NEW subscriber')
    
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
                        "phone_number": subscriber.phone_number,
                        "email": subscriber.email,
                      },
                      "content": {
                       "title": "Hackathon Alert",
                       "body": "Hiya "+ subscriber.name +"! A hackathon called "+ contest.name +" is starting in the next 24 hours!! Check it out at "+ contest.url,
                      },
                      "data": {
                        "name": subscriber.name,
                      },
                      "routing": {
                        "method": "all",
                        "channels": ["email", "sms"],
                      },
                    }
                  )
                print(resp['requestId'])
                print('messeges sent to subscribers list')