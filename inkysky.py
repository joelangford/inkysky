import requests, sched, time
from utils.convertToCelcius import convertToCelcius;
from modules.percipGraphHour import percipGraphHour;
from modules.temperatureGraphDay import temperatureGraphDay;
from print.print import printToInky

apiKey = ''
londonLngLat = '51.5618462,-0.017913'
newcastleLngLat = '54.9771,-1.6142'
s = sched.scheduler(time.time, time.sleep)

try:
    with open('apikey', 'r') as file:
        apiKey = file.read().replace('\n', '')
except EnvironmentError:
    print('Unable to find darksky apikey, please add darksky api key to a file named "apikey" at the root')


def updateWeather(sc):
    response = requests.get("https://api.darksky.net/forecast/" + apiKey + "/" + londonLngLat)
    currentTempF = response.json()['currently']['temperature']
    curentTempC = round(convertToCelcius(currentTempF),2)

    minutelyData = response.json()['minutely']['data']
    hourlyData = response.json()['hourly']['data']
    nextHourSummary = response.json()['minutely']['summary']
    icon = response.json()['currently']['icon']

    # percipGraphHour(minutelyData)
    temperatureGraphData = temperatureGraphDay(hourlyData)

    printToInky(str(curentTempC) + " °C", nextHourSummary, icon, temperatureGraphData)

    s.enter(120, 1, updateWeather, (sc,))

if len(apiKey) > 1: 
    s.enter(0, 1, updateWeather, (s,))
    s.run()
