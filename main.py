#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import *
from flight_search import *
from datetime import datetime, date , timedelta

from flight_data import *


today=date.today()
tomorrow=str(today+timedelta(days=1))
six_months=str(today+timedelta(days=1))
city_start="CTA"


date_from=datetime(2022,7,10)
date_to=datetime(2022,7,11)
return_from=datetime(2022,7,15)
return_to=datetime(2022,7,16)
flight_type="round"
max_stopovers="1"

wish_list=DataManager()
print(wish_list)
wish_list=wish_list['prices']

pr=FlightData()

for destination in wish_list:

    city=destination['iataCode']
    threshold=destination['lowestPrice']


    My_Flight= FlightSearch(city_start,city,date_from, date_to, return_from, return_to, flight_type )

    pr.structure(My_Flight, threshold)
print(pr.df)
pr.df.to_excel("results.xlsx")


#print(lista)

#print(wish_list)
