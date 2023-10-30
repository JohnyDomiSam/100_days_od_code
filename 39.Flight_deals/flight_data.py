import requests
from datetime import datetime, timedelta
from pprint import pprint


class FlightData:

    def __init__(self, departure):
        self.now = datetime.now()
        self.today = self.now.today()
        self.today_f = self.today.strftime("%d/%m/%Y")
        self.tomorrow = self.today + timedelta(1)
        self.tomorrow_f = self.tomorrow.strftime("%d/%m/%Y")
        self.in_six_months = self.today + timedelta(180)
        self.in_six_months_f = self.in_six_months.strftime("%d/%m/%Y")
        self.return_from = self.today + timedelta(7)
        self.return_from_f = self.return_from.strftime("%d/%m/%Y")
        self.return_to = self.today + timedelta(14)
        self.return_to_f = self.return_to.strftime("%d/%m/%Y")
        self.url = "https://api.tequila.kiwi.com/v2/search"
        self.headers = {"apikey": "cYunW0d0DZOSaDn-1pnluB0MMhL3KGgy"}
        self.parameters = {"fly_from": "LON",
                           "fly_to": departure,
                           "date_from": self.tomorrow_f,
                           "date_to": self.in_six_months_f,
                           "return_from": self.return_from_f,
                           "return_to": self.return_to_f,
                           "curr": "EUR",
                           "ret_from_diff_city": "false",
                           "ret_to_diff_city": "false",
                           "max_stopovers": 0}
        self.data = self.get_price()
        self.list_of_its = self.data["data"]
        self.lowest_fair = self.get_lowest_price()
        self.lowest_price = self.lowest_fair["price"]
        self.o_date = self.get_o_date()
        self.i_date = self.get_i_date()

    def get_price(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.parameters)
        response.raise_for_status()
        data = response.json()
        return data

    def get_lowest_price(self):
        list_of_prices = []
        for its in self.list_of_its:
            list_of_prices.append(its["price"])
        min_price = min(list_of_prices)
        list_index = list_of_prices.index(min_price)
        return self.list_of_its[list_index]

    def get_o_date(self):
        date_time_list = self.lowest_fair["local_departure"].split("T")
        date = date_time_list[0]
        time = date_time_list[1][:5]
        return date, time

    def get_i_date(self):
        date_time_list = self.lowest_fair["local_arrival"].split("T")
        date = date_time_list[0]
        time = date_time_list[1][:5]
        return date, time
