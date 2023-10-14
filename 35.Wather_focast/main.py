import requests
from twilio.rest import Client
import os


course_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("api_key")
course_key = os.environ.get("course_key")

account_sid = 'AC89d90d3e2bc457fe9433e12f1d26f32d'
auth_token = os.environ.get("auth_token")

parameters = {"lat": 49.437939,
              "lon": 18.789700,
              "appid": course_key,
              "units": "metric",
              "exclude": "minutely,daily,current"}

def is_raining() -> bool:
    response = requests.get(course_endpoint, params=parameters)
    response.raise_for_status()
    data = response.json()
    for hour in range(12):
        id = data["hourly"][hour]["weather"][0]["id"]
        if id < 700:
            return True
    return False

if is_raining():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain today, bring an umbrella !",
        from_='+18182931791',
        to='+421905555555'
    )
    print(message.status)