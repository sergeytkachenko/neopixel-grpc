FROM python:3
RUN pip3 install adafruit-circuitpython-neopixel RPi.GPIO rpi-ws281x
WORKDIR /app
COPY neopixel-interface.py neopixel-interface.py
ENTRYPOINT ["python", "neopixel-interface.py"]