import json
from . import models

URL = "https://www.kontests.net/api/v1/all"

def getContests(request):
    contests = json.dumps(request.text(URL), indent=4)
    print(contests)