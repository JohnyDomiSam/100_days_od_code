import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 48.716385
MY_LONG = 21.261074
my_email = "my_email@gmail.com"
password = "my_password"
rec_email = "rec_email@gmail.com"
new_letter = "ISS if flying over your head, look up !"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_over_you():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
    else:
        print("Not over you.")
        lat_off = round(MY_LAT - iss_latitude)
        long_off = round(MY_LONG - iss_longitude)
        print(f"ISS position is {iss_latitude}, {iss_longitude}.")
        print(f"ISS if of from your location by {lat_off}, {long_off}")


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour > sunset < sunrise:
        return True


while True:
    time.sleep(5)
    if is_over_you() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=rec_email,
                msg=f"Subject:ISS over you !\n\n{new_letter}")
