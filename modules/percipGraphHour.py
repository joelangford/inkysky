def percipGraphHour(data):
    for minute in data:
        if minute['precipProbability'] > 0.5:
            print(minute['precipProbability'] * 100,"% chance of rain starting in",((minute['time'] - time.time())/ 60),"minutes")
            break
