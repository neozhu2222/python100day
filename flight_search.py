import requests
from flight_data import FlightData
TEQUILLA_ENDPOINT = tequilla_api_url
TEQUILLA_API = tequilla_api_key


class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILLA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILLA_API}
        query = {"term": city_name, "location_types": city}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self):
        headers = {"apikey": TEQUILLA_API}
        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": from_time.strftime(%d/%m/%Y),
            "date_to": to_time.strftime(%d/%m/%Y),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILLA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {DEST_CITY_CODE}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data