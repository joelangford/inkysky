from collections import OrderedDict
from datetime import datetime

def percipGraphHour(data):
    precipitation = OrderedDict()

    for idx, minute in enumerate(data):
        precipIntensityPercentage = round((minute['precipIntensity']) * 1000 / 3)
        time = int(datetime.utcfromtimestamp(minute['time']).strftime('%M'))
        # print(str(precipIntensityPercentage) + ' ' + str(time))

        if time % 5 == 0:
            precipitation[time] = {
                'time' : time,
                'precipIntensityPercentage': precipIntensityPercentage
            }
        else:
            targetIndex = time - (time % 5)
            print(targetIndex)
            # precipitation[targetIndex]['precipIntensityPercentage'] = round((precipitation[targetIndex]['precipIntensityPercentage'] + precipIntensityPercentage) / (time % 5), 1)

    print(precipitation)

    return
