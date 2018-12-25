from random import randint
from time import sleep

class Twinkle:
    def run(self, mote):
        channel = randint(1, 4)
        pixel = randint(0, 15)

        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        mote.set_pixel(channel, pixel, red, green, blue)
        mote.show()
        sleep(0.2)
