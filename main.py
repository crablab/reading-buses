from reading_buses import stop
import os

API_KEY = os.getenv('READING_BUSES_KEY')

southcote_road = stop.stop(API_KEY, '039027230003')

data = southcote_road.getNextBuses() 

print(data)