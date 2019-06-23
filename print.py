from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.BLACK)

def printToInky(temperature, summary):
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    draw.rectangle((0,0,inky_display.WIDTH, inky_display.HEIGHT), inky_display.BLACK)

    temperatureFont = ImageFont.truetype(FredokaOne, 22)
    draw.text((10, 10), temperature, inky_display.WHITE, temperatureFont)

    summaryFont = ImageFont.truetype(FredokaOne, 12)
    draw.text((10, 40), summary, inky_display.WHITE, summaryFont)

    icon = Image.open("icon-sun.png")
    # get the correct size
    x, y = icon.size
    draw.paste(icon, (0,50,x,y))

    inky_display.set_image(img)
    inky_display.show()
