import time
import board
import neopixel
import sys

pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB
OPACITY = float(sys.argv[5])
COLOR = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
PIXEL_INDEX = int(sys.argv[1])
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=OPACITY, auto_write=False, pixel_order=ORDER)
pixels[PIXEL_INDEX] = COLOR
