import datetime
from .sendEmails import sendEmail

def timer():
    time = datetime.datetime.now()
    sendtime = time.strftime("%A")
    print (time)
    if sendtime == "Monday":
        sendEmail()