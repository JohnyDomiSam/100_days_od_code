from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3687d433972e8fcfb23bbd169b72b3db/flightDeals/prices"
HEADER = {"Authorization": "Bearer huasfhauihfif",
          "Content-Type": "application/json"
          }


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, headers=HEADER
            )
            response.raise_for_status()

    def update_price(self, price, city):
        row_id = 0
        for ds in self.destination_data:
            if ds["city"] == city:
                row_id = ds["id"]

        updated_price = {"price": {
            "lowestPrice": price
        }}
        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
                                headers=HEADER,
                                json=updated_price)
        response.raise_for_status()

