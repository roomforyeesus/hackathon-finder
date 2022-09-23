import sys
from trycourier import Courier
from . models import Subscriber



client = Courier(auth_token=".env.courierapikey")

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
      "name": "Peter Parker",
    },
    "routing": {
      "method": "single",
      "channels": ["email"],
    },
  }
)

print(resp['messageId'])
