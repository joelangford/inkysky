import glob
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from print.createMask import createMask

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

def printToInky(temperature, summary, iconType):
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

    inky_display.set_image(img)
    inky_display.show()
