import requests
from .models import Contests

URL = "https://www.kontests.net/api/v1/all"

def getContests():
    response = requests.get(URL)
    data = response.json()
    for contest in data:
        Contests.objects.create(
            name=contest['name'],
            url=contest['url'],
            start_time=contest['start_time'],
            end_time=contest['end_time'],
            duration=contest['duration'],
            in_24_hours=contest['in_24_hours']
        )
        
    return data