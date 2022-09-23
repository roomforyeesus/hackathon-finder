import requests
from .models import Contest

URL = "https://www.kontests.net/api/v1/all"

def getContests():
    response = requests.get(URL)
    data = response.json()
    for contest in data:
        Contest.objects.create(
            name=contest['name'],
            url=contest['url'],
            start_time=contest['start_time'],
            end_time=contest['end_time'],
            duration=contest['duration'],
            description=contest['description'],
            in_24_hours=contest['in_24_hours']
        )
    print('contests saved')
    return data