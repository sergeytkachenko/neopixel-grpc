import time
import board
import neopixel
import sys

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 16

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
pixels.fill((255, 0, 0))
# Uncomment this line if you have RGBW/GRBW NeoPixels
# pixels.fill((255, 0, 0, 0))
pixels.show()
time.sleep(1)

# Comment this line out if you have RGBW/GRBW NeoPixels
pixels.fill((0, 255, 0))
# Uncomment this line if you have RGBW/GRBW NeoPixels
# pixels.fill((0, 255, 0, 0))
pixels.show()
time.sleep(1)

# Comment this line out if you have RGBW/GRBW NeoPixels
pixels.fill((0, 0, 255))

COLOR = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]))
print(COLOR)
pixels[int(sys.argv[1])] = COLOR
# pixels.fill((0, 0, 255, 0))
pixels.show()