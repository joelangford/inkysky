from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

def printToInky(temperature, summary):
    temperatureFont = ImageFont.truetype(FredokaOne, 22)
    draw.text((10, 10), temperature, inky_display.BLACK, temperatureFont)

    summaryFont = ImageFont.truetype(FredokaOne, 12)
    draw.text((10, 40), summary, inky_display.BLACK, summaryFont)

    inky_display.set_image(img)
    inky_display.show()
