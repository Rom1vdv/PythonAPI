import requests
import json
import dotenv
import os

dotenv.load_dotenv()

KEY = os.getenv("API_KEYS")

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
LOCATION = "Brussels" # Format is address, partial address, longitude|latitude combo
DATE_1 = "/2024-01-29" #Format is /yyyy-MM-dd
DATE_2 = "/2024-01-30"
UNIT_GROUP = "metric"
CONTENT_TYPE = "json"



request = requests.get(f"{URL}{LOCATION}{DATE_1}{DATE_2}?unitGroup={UNIT_GROUP}&key={KEY}&contentType={CONTENT_TYPE}")
print(request)
jsondata = request.json()

print(json.dumps(jsondata, indent=4), file=open("weather.txt", "w"))

