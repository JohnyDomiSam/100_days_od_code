from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Create data_manager object from DataManager class
data_manager = DataManager()
sheet_data = data_manager.sheet_data

# Replace IATA codes in dict with actual iata codes of city airports if empty
if sheet_data[0]["iataCode"] == "":
    for dict in sheet_data:
        city = dict["city"]
        flight_search = FlightSearch(city=city)
        iata = flight_search.get_iata()
        dict["iataCode"] = iata
        new_row = {"price": dict}
        id = dict["id"]
        data_manager.edit_iota(row=new_row, id=id)
# Print city and lowers price of round trip from London in 6 months
best_prices = {}
for d in sheet_data:
    departure = d["iataCode"]
    city = d["city"]
    fd = FlightData(departure=departure)
    best_prices[city] = fd.lowest_price
    print(f"{city}: {fd.lowest_price}€ date: {fd.o_date[0]} time: {fd.o_date[1]}")
    if d["lowestPrice"] > best_prices[d["city"]]:
        notification = NotificationManager(price=fd.lowest_fair["price"],
                                           dep_city_name=fd.lowest_fair["cityFrom"],
                                           dep_iata_code=fd.lowest_fair["cotyCodeFrom"],
                                           arr_city_name=fd.lowest_fair["cityTo"],
                                           arr_airport_iata=fd.lowest_fair["cityCodeTo"],
                                           o_date=fd.o_date(),
                                           i_date=fd.i_date())
        notification.send_telegram()

