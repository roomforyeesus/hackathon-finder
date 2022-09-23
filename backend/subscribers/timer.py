import datetime
from .sendEmails import sendEmail

def timer():
    time = datetime.datetime.now()
    sendtime = x.strftime("%A")
    print (time)
    if sendtime == "Monday":
        sendEmail()