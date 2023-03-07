import requests
import json
import pandas as pd
API_ENDPOINT_PRICES="https://api.sheety.co/d1aaeb0f57e07899af67fe9e17c3e0dd/flightDeals/prices"
API_ENDPOINT_USERS="https://api.sheety.co/d1aaeb0f57e07899af67fe9e17c3e0dd/flightDeals/users"



def DataManager():
        try:
            with open("data.json", mode="r") as file:
                data=json.load(file)
            return data
        except FileNotFoundError:
            response = requests.get(url=API_ENDPOINT_PRICES)
            response.raise_for_status()
            data=response.json()
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            return data


