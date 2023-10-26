import requests


class DataManager:

    def __init__(self):
        self.url = "https://api.sheety.co/3687d433972e8fcfb23bbd169b72b3db/flightDeals/prices"
        self.header = {"Authorization": "Bearer huasfhauihfif",
                       "Content-Type": "application/json"
                       }
        self.sheet_data = self.get_data(self.url, self.header)

    def get_data(self, url, header):
        url = self.url
        header = self.header
        response = requests.get(url=url, headers=header)
        response.raise_for_status()
        data = response.json()["prices"]
        return data

    def edit_iota(self, row, id):
        url = f"https://api.sheety.co/3687d433972e8fcfb23bbd169b72b3db/flightDeals/prices/{id}"
        response = requests.put(url=url, headers=self.header, json=row)
        response.raise_for_status()
