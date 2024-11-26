import requests
from twilio.rest import Client
import os
()
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
api_key = os.environ.get("api_key")

parameters = {"lat":4.041673, #DOUALA LOCATION
              "lon":9.706788,
              "cnt":4,
"appid":api_key}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

d = data["list"][0]["weather"][0]["id"]

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body='ITS IS RAINING IN DOUALA FROM UR SON 🥹',
             from_='+13254253823',
             to='+2347061533400'
         )

    print(message.status)