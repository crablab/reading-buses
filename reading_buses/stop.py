import requests
import xmltodict
from datetime import datetime, timezone
import logging

class stop:

  def __init__(self, apiKey, stopID) -> None:
      self.apiKey = apiKey
      self.stopID = stopID

  def get(self):
    response = requests.get('https://reading-opendata.r2p.com/api/v1/siri-sm', params={'api_token': self.apiKey, 'location': self.stopID})

    return xmltodict.parse(response.content)

  def getNextBuses(self):
    data = self.get()
    nextBuses=[]

    for bus in data['Siri']['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']:
      try:
        line = bus['MonitoredVehicleJourney']['LineRef']
        due_in = datetime.fromisoformat(bus['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']) - datetime.now(timezone.utc)
        nextBuses.append([line, due_in])
      except KeyError:
        logging.debug("Bus missing required data")

    return nextBuses