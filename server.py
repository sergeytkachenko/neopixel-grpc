import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import simplejson
import board
import neopixel

pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB
opacity = 0.3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=opacity, auto_write=False, pixel_order=ORDER)

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 80

class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == '/':
            self.setPixels()

    def setPixels(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = simplejson.loads(self.data_string)
        print(data['pixels'])
        pixels.brightness = float(data['opacity'])
        for pixel in data['pixels']:
            index = int(pixel['index'])
            red = int(pixel['r'])
            green = int(pixel['g'])
            blue = int(pixel['b'])
            pixels[index] = (red, green, blue)

        pixels.show()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('{"success": true}'.encode("UTF-8")))

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))