from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

def printToInky(text):
    inky_display = InkyPHAT("yellow")
    inky_display.set_border(inky_display.WHITE)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(FredokaOne, 22)

    message = text
    w, h = font.getsize(message)
    x = 10
    y = 10

    draw.text((x, y), message, inky_display.BLACK, font)
    inky_display.set_image(img)
    inky_display.show()
