import glob
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from print.createMask import createMask

heeboFontPath = "fonts/heebo/Heebo-Regular.ttf"
inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.BLACK)

icons = {}
masks = {}

# Load our icon files and generate masks
for icon in glob.glob("icons/icon-*.png"):
    icon_name = icon.split("icon-")[1].replace(".png", "")
    icon_image = Image.open(icon)
    icons[icon_name] = icon_image
    masks[icon_name] = createMask(icon_image)

# This maps the weather summary from Dark Sky
# to the appropriate weather icons
icon_map = {
    "snow": ["snow", "sleet"],
    "rain": ["rain"],
    "cloud": ["fog", "cloudy", "partly-cloudy-day", "partly-cloudy-night"],
    "sun": ["clear-day", "clear-night"],
    "storm": [],
    "wind": ["wind"]
}

def buildGraph(data, high, low):
    graphAreaHeight = 40
    maxBarHeight = 30
    graph = Image.new("P", (inky_display.WIDTH, graphAreaHeight), inky_display.BLACK)
    draw = ImageDraw.Draw(graph)
    barFrameWidth = int(round(inky_display.WIDTH / 12))
    barWidth = barFrameWidth - 4
    graphFont = ImageFont.truetype(heeboFontPath, 8)
    xOffset = 4
    
    for idx, entry in enumerate(data):
        temperature = str(round(data[entry]['temperature'])) + "°"
        percent = (data[entry]['temperature'] / high) * 100
        hour = (data[entry]['time'])
        
        barX = int((barFrameWidth * idx) + (barFrameWidth / 2) - xOffset)
        barY = int(maxBarHeight - (maxBarHeight * (percent / 100)))
        draw.line((barX, barY, barX, maxBarHeight), inky_display.RED, barWidth)  

        temperatureTextSizeX, temperatureTextSizeY = graphFont.getsize(temperature)
        hourTextSizeX, hourTextSizeY = graphFont.getsize(hour)

        draw.text((barX - (hourTextSizeX / 2), barY), temperature, inky_display.BLACK, graphFont, align="center")
        draw.text((barX - (hourTextSizeX / 2), maxBarHeight), hour, inky_display.WHITE, graphFont, align="center")
    return graph

def printToInky(temperature, summary, iconType, temperatureGraphData):
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)
    draw = ImageDraw.Draw(img)

    temperatureFont = ImageFont.truetype(FredokaOne, 22)
    draw.text((10, 10), temperature, inky_display.WHITE, temperatureFont)

    summaryFont = ImageFont.truetype(FredokaOne, 12)
    draw.text((10, 40), summary, inky_display.WHITE, summaryFont)

    for icon in icon_map:
        if iconType in icon_map[icon]:
            weather_icon = icon
            break

    if weather_icon is not None:
        iconXposition = inky_display.WIDTH - icons[weather_icon].size[0]
        img.paste(icons[weather_icon], (iconXposition, 0), masks[weather_icon])

    else:
        draw.text((28, 36), "?", inky_display.YELLOW, font=summaryFont)
    
    graph = buildGraph(temperatureGraphData[0], temperatureGraphData[1], temperatureGraphData[2])
    img.paste(graph, (0, inky_display.HEIGHT - 40))

    img = img.rotate(180, expand=True)

    inky_display.set_image(img)
    inky_display.show()
