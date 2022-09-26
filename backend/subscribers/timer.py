import datetime
from .sendEmails import sendEmail
from .hackathonData import getContests

def timer():
    time = datetime.datetime.now()
    sendtime = time.strftime("%A") 
    print (sendtime)
    if sendtime == "Monday" or sendtime == "Saturday" or sendtime == "Wednesday":
        sendEmail()
        count = 0
        if count <3:
            count += 1
        else:
            getContests()
            count = 0
    else:
        print('no messeges sent')
        pass
