from pprint import pprint
import requests
SHEETY_PRICE_END = sheety_price_end_url

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_END)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_dest_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICE_END/{city['id']}",
                json=new_data
            )
