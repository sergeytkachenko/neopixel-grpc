FROM python:3
RUN pip3 install adafruit-circuitpython-neopixel RPi.GPIO rpi-ws281x
RUN wget https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz \
    && tar -xvf go1.13.3.linux-amd64.tar.gz \
    && mv go /usr/local
ENV GOROOT=/usr/local/go
WORKDIR /app
COPY neopixel-interface.py neopixel-interface.py
ENTRYPOINT ["python", "neopixel-interface.py"]