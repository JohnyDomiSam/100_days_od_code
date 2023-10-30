import requests


class NotificationManager:

    def __init__(self, price, dep_city_name, dep_iata_code, arr_city_name, arr_airport_iata, o_date, i_date):
        self.message = f'Low price alert!\nOnly {price} to fly from {dep_city_name}-{dep_iata_code} to {arr_city_name}-{arr_airport_iata},\nfrom {o_date} to {i_date}'
        self.chat_id = "1383520281"
        self.URL = "https://api.telegram.org/bot6769511991:AAGTePHE8DMpUVITwrJVIwnbcQVVdN9lWRI/sendMessage"
        self.parameters = {"chat_id": self.chat_id,
                           "text": self.message}

    def send_telegram(self):
        self.response = requests.post(url=self.URL, params=self.parameters)
        self.response.raise_for_status()
