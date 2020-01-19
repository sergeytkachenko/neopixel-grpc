FROM debian:stretch
WORKDIR /app
COPY neopixel-interface.py neopixel-interface.py
ENTRYPOINT ["phyton3", "neopixel-interface.py"]