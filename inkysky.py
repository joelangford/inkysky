import requests, sched, time
from utils.convertToCelcius import convertToCelcius;
from modules.percipGraphHour import percipGraphHour;
from print.print import printToInky

londonLngLat = '51.5618462,-0.017913'
newcastleLngLat = '54.9771,-1.6142'
apiKey = '7b0d66c29543af4b6eadef1d236e2fc8'
s = sched.scheduler(time.time, time.sleep)

def updateWeather(sc):
    response = requests.get("https://api.darksky.net/forecast/" + apiKey + "/" + londonLngLat)
    currentTempF = response.json()['currently']['temperature']
    curentTempC = round(convertToCelcius(currentTempF),2)

    nextHourData = response.json()['minutely']['data']
    nextHourSummary = response.json()['minutely']['summary']
    icon = response.json()['currently']['icon']

    percipGraphHour(nextHourData)

    printToInky(str(curentTempC) + " °C", nextHourSummary, icon)

    s.enter(120, 1, updateWeather, (sc,))

s.enter(0, 1, updateWeather, (s,))
s.run()
