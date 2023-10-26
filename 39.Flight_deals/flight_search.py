import requests

class FlightSearch:

    def __init__(self, city):
        self.url = "https://api.tequila.kiwi.com/locations/query"
        self.headers = {"apikey": "cYunW0d0DZOSaDn-1pnluB0MMhL3KGgy"}
        self.parameters = {"term": city,
                           "location_types": "city"}


    def get_iata(self):
        response = requests.get(url=self.url, params=self.parameters, headers=self.headers)
        response.raise_for_status()
        city_data = response.json()
        return city_data["locations"][0]["code"]


