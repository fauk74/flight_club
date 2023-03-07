

import requests
from datetime import datetime

API_ENDPOINT="https://tequila-api.kiwi.com/v2/search"
TOKEN="JB0iZ_Vz3Wg9an9TcPehgAxMLPWCVBSK"
headers={"apikey": TOKEN}




#class FlightSearch:
#    def __init__(self):
#        self.city_codes=[]

#    def get_destinations(selfself, city_names):


def FlightSearch(city_from, city_to,date_from, date_to, return_from, return_to, flight_type):
    #  def __init__(self):

    #    Inquiry = "fly_from=" + city_from + "&fly_to="+city_to+"&date_From=" + date_from.strftime("%d/%m/%Y") + "&date_To=" + date_to.strftime("%d/%m/%Y")+"&return_From="+return_from.strftime("%d/%m/%Y")+"&return_To="+return_to.strftime("%d/%m/%Y")+"&flight_Type="+flight_type
                  #+"&flight_type="+flight_type+"&max_stopovers="+max_stopovers
        Inquiry={"fly_from": city_from,
                 "fly_to": city_to,
                 "date_from": date_from.strftime("%d/%m/%Y"),
                 "date_to":date_to.strftime("%d/%m/%Y"),
                 "return_from": return_from.strftime("%d/%m/%Y"),
                 "return_to":return_to.strftime("%d/%m/%Y"),
                 "flight_type":flight_type}


        #Inquiry = API_ENDPOINT + "fly_from=" + city_from + "&fly_to=" + city_to + "&dateFrom=" + from_date + "&dateTo=" + to_date
        response=requests.get(API_ENDPOINT, headers=headers, params=Inquiry)
        response.raise_for_status()
        return response.json()
