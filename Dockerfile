FROM debian:stretch
WORKDIR /app
COPY neopixel-interface.py neopixel-interface.py
ENTRYPOINT ["python", "neopixel-interface.py"]