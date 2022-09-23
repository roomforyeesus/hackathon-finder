from django.http import JsonResponse
import json 
import requests

url = "https://www.kontests.net/api/v1/all"

async def getContests(request):
    print ("hitting the getContests method")
    response = requests.get(url)
    data = await json.loads(response.text)
    print (data)
        
        
getContests(url)