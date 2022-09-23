import os 
from dotenv import load_dotenv
from . models import Contest, Subscriber
from . import hackathonData
from trycourier import Courier
import requests

load_dotenv()
APIKEY = os.getenv('courierapikey')


def sendEmail():
    print('hitting the sendEmail method')
    client = Courier(auth_token="APIKEY")

    resp = client.send_message(
  message={
    "to": {
      "email": Subscriber.email,
    },
    "content": {
      "title": "Welcome!",
      "body": "Thanks for signing up, {{Subscriber.name}}!",
    },
    "data": {
    },
    "routing": {
      "method": "single",
      "channels": ["email"],
    },
  }
)

    print(resp['messageId'])


