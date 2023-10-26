import requests
from datetime import datetime
import os

EXCERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {"x-app-id": APP_ID,
           "x-app-key": API_KEY}


excercise_prompt = input("Which excercise you did ?")
parameters = {"query": excercise_prompt,
              "gender": "male",
              "weight_kg": 89,
              "height_cm": 182,
              "age": 34
              }
# Nutritionx post request
response = requests.post(url=EXCERCISE_URL, headers=headers, json=parameters)
data = response.json()

today = datetime.now()
date = today.strftime("%Y/%m/%d")
time = today.strftime("%H:%M:%S")
new_dict = {"date": date,
            "time": time,
            "exercise": data["exercises"][0]["name"].title(),
            "duration": data["exercises"][0]["duration_min"],
            "calories": data["exercises"][0]["nf_calories"]}

# Sheety congig
new_record = {"workout": new_dict}
bearer_token = os.environ.get("Bearer")
sheety_header = {"Content-Type": "application/json",
                 "Authorization": bearer_token}

sheety_url = os.environ.get("sheety_url")
sheety_response = requests.post(url=sheety_url, json=new_record, headers=sheety_header)
sheety_response.raise_for_status()
