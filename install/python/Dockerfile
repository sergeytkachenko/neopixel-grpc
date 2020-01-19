FROM python:3
RUN pip3 install adafruit-circuitpython-neopixel RPi.GPIO rpi-ws281x simplejson
WORKDIR /app
COPY server.py server.py
EXPOSE 80
ENTRYPOINT ["python", "server.py"]