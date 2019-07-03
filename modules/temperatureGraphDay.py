from datetime import datetime
from utils.convertToCelcius import convertToCelcius;

def temperatureGraphDay(data):
    high = 0
    low = 0

    temperatures = {}

    for idx, hour in enumerate(data):
        degreesCelcius = convertToCelcius(hour['temperature'])
        time = datetime.utcfromtimestamp(hour['time']).strftime('%H')

        if degreesCelcius > high:
            high = round(degreesCelcius, 1)

        if degreesCelcius < low:
            low = round(degreesCelcius, 1)

        if idx == 0:
            low = round(degreesCelcius, 1)

        if idx % 2 == 0:
            temperatures[idx] = {
                'time' : time,
                'temperature': degreesCelcius
            }
        else:
            temperatures[idx - 1]['temperature'] = round((temperatures[idx - 1]['temperature'] + degreesCelcius) / 2,1)

        if idx == 23 :
            break

    return(temperatures, high, low)
