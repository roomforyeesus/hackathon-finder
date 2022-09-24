import datetime
from .sendEmails import sendEmail
from .hackathonData import getContests

def timer():
    time = datetime.datetime.now()
    sendtime = time.strftime("%A") 
    print (sendtime)
    if sendtime == "Monday" or sendtime == "Saturday" or sendtime == "Wednesday":
        getContests()
        sendEmail()
    else:
        print('no email sent')
        pass