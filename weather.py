import requests
import json

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
KEY = "BCYAU98N2ZNJCKNQD68VTMW7M"
LOCATION = "Brussels"
UNIT_GROUP = "metric"
CONTENT_TYPE = "json"



request = requests.get(f"{URL}{LOCATION}?unitGroup={UNIT_GROUP}&key={KEY}&contentType={CONTENT_TYPE}")

jsondata = request.json()

print(json.dumps(jsondata, indent=4), file=open("weather.txt", "w"))

