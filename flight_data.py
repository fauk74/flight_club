import pandas as pd


class FlightData():
#    #def This class is responsible for structuring the flight data.
    def __init__(self):
        self.df=pd.DataFrame(columns=['cityCodeFrom', 'cityCodeTo','duration','price','deep_link','local_arrival','local_departure'])
#        pass

    def structure(self,  JSON, threshold):

        Data=JSON['data']
        for a in Data:
            self.id=a['id']
            self.cityCodeFrom=a['cityCodeFrom']
            self.cityCodeTo=a['cityCodeTo']
            self.duration=a['duration']['total'],
            self.price=a['price']
            self.link=a['deep_link']
            self.local_arrival=a['local_arrival']
            self.local_departure=a['local_departure']
            b=pd.DataFrame([[self.cityCodeFrom,
                            self.cityCodeTo,
                            self.duration,
                            self.price,
                            self.link,
                            self.local_arrival,
                            self.local_departure
                            ]],
                           columns=['cityCodeFrom', 'cityCodeTo','duration','price','deep_link','local_arrival','local_departure'],
                           index=[id])
            if self.price <= threshold:
                self.df=pd.concat([self.df,b])

        return