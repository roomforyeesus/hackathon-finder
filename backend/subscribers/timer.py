import datetime
from .sendEmails import sendEmail
from .hackathonData import getContests

def timer():
    time = datetime.datetime.now()
    sendtime = "Monday" #time.strftime("%A")
    print (time)
    if sendtime == "Monday":
        getContests()
        sendEmail()